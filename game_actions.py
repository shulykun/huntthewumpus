import numpy as np
import re
import vectorizer as v

from replics import Replics


class Actions():

    def __init__(self):
        self.replics = Replics()
        self.rooms_count = 20
        self.game_objects = {}
        self.game_spacegame_rooms = {}
        self.game_user = {}


    def init_user_state(self):
        '''Характеристики игрока'''
        a = {
             'arrows':5,
             'lives':1
        }

        return a


    def init_game_space(self):
        '''Генерация лабиринта'''
        space =[]

        def min_treshold(x, x_thresh, x_replace):
            return x_replace if x < x_thresh else x

        def max_treshold(x, x_thresh, x_replace):
            return x_replace if x > x_thresh else x

        for i in range(5):
            space.append([max_treshold(i+1,4,0), min_treshold(i-1, 0, 4), i+5])

        for i in range(5,10):
            space.append([min_treshold(i+4, 10, 14), i+5,  i-5])

        for i in range(10,15):
            space.append([max_treshold(i-4,9,5), i-5, i+5])

        for i in range(15,20):
            space.append([max_treshold(i+1,19,15), i-1, i-5])
        return space


    def init_game_objects(self,rooms):
        '''Расстановка объектов в игре'''

        def room_object(exclude_rooms, n_rooms=1):
            r = []
            while len(r) < n_rooms:
                n = np.random.randint(self.rooms_count)
                if n not in exclude_rooms:
                    r.append(n)
            return r

        def rooms_exclude(g_objects):
            return [item for sublist in g_objects.values() for item in sublist]


        g_objects = {
                     'wampus':room_object([])
                    }

        for i in ['holes','bats']:

            g_objects[i] = room_object(rooms_exclude(g_objects), n_rooms=2)

        for i in ['holes','bats','wampus']:
            g_objects[i+'_near'] = [item for sublist in [rooms[i] for i in g_objects[i]]  for item in sublist]

        g_objects['player_history'] = room_object(rooms_exclude(g_objects))

        return g_objects


    def check_active_user(f):
        def wrapper(self, n):
            if self.game_user['lives'] > 0:
                return f(self, n)
            else:
                return self.replics.game_over()

        return wrapper


    def set_game_space(self):
        self.game_space = self.init_game_space()


    def set_game_objects(self):
        self.game_objects = self.init_game_objects(self.game_space)


    def set_game_user(self):
        self.game_user = self.init_user_state()


    def create_game_world(self):
        '''Создание мира игры - генерация лабиринта
            и размещение всех объектов - мыши, ямы, Вампус, игрок'''
        self.set_game_space()
        self.set_game_objects()
        self.set_game_user()


    def append_history(self,room_to):
        '''Добавление посещенной комнаты в историю'''
        self.game_objects['player_history'].append(room_to)


    def start(self, input_seq):
        '''Запуск игры'''

        self.create_game_world()
        player_start_room = self.game_objects['player_history'][0]

        return self.replics.start_game(player_start_room,self.game_space[player_start_room])


    def restart(self, input_seq):
        '''Перезапуск игры'''
        self.create_game_world()
        player_start_room = self.game_objects['player_history'][0]

        return self.replics.restart_game(player_start_room,self.game_space[player_start_room])


    def not_found(self, input_seq):
        '''Не распознан запрос'''

        return self.replics.not_found()


    @check_active_user
    def move_room(self, input_seq):
        '''Переход в комнтау - обработка тектового запроса'''

        n = v.find_numbers(input_seq)

        if len(n) == 1:

            room_to = int(n[0])
            room_from = int(self.game_objects['player_history'][-1])

            response = self.move_room_process(room_to, room_from)

        else:
            response = self.replics.move_wrong_input()

        return response


    def move_room_process(self, room_to, room_from, check_connection=True):
        '''Фиксация перехода в комнату и проработка игровых послествий
        - встреча с объектами, запись в историю'''

        if check_connection:
            if room_to in self.game_space[room_from]:
                self.append_history(room_to)
                return  self.move_check_room(room_to)

            if room_to == room_from:
                return self.replics.move_room_same(room_to, self.game_space[room_to])

            else:
                return self.replics.move_room_close(room_from, room_to, self.game_space[room_from])
        else:
            self.append_history(room_to)
            return self.move_check_room(room_to)


    def move_room_bats(self, room_to, rooms_connect):
        '''Последствия перехода в комнату с мышами - перенос в случайную комнату'''

        room_forward = room_to
        while room_forward == room_to:
            room_forward = np.random.randint(self.rooms_count)

        response_ = self.replics.move_room_bats()
        response = self.move_room_process(room_forward, room_to, check_connection=False)


        return '{} {}'.format(response_,response)


    def move_room_holes(self, room_to, rooms_connect):

        self.game_user['lives'] -= 1
        return self.replics.move_room_holes(room_to, rooms_connect)


    def move_room_wampus(self, room_to, rooms_connect):

        self.game_user['lives'] -= 1
        return self.replics.move_room_wampus(room_to, rooms_connect)


    def move_check_room(self,room_to):
        '''Проверка открытой игроком комнаты на все игровые предметы.
        Выбор функции для ответа.'''
        check_state_func = {
                       'wampus':self.move_room_wampus,
                       'holes':self.move_room_holes,
                       'bats':self.move_room_bats,
                       'holes_near':self.replics.move_room_holes_near,
                       'bats_near':self.replics.move_room_bats_near,
                       'wampus_near':self.replics.move_room_wampus_near
                    }

        for c in check_state_func.keys():
            if room_to in self.game_objects[c]:
                f = check_state_func[c]

                return f(room_to, self.game_space[room_to])

        return self.replics.move_room_empty(room_to, self.game_space[room_to])


    def shoot_random_rooms(self, rooms_arrow_pass, room_prev):
        '''Генерация случайного полета стрелы с момента ошибки в комнате'''

        while len(rooms_arrow_pass) < 5:

            room_connect = self.game_space[room_prev]
            room_target = np.random.choice(room_connect,1)[0]

            if room_target not in rooms_arrow_pass:
                rooms_arrow_pass.append(room_target)
                room_prev = room_target

        return rooms_arrow_pass


    def shoot_check_rooms(self, rooms_arrow, player_room):
        '''Определение комнат через которые на самом деле пролетела стрела'''

        wrong_room = False

        room_prev = player_room

        rooms_arrow_pass = []

        for room_target in rooms_arrow:

            room_connect = self.game_space[room_prev]

            if room_target not in room_connect:

                rooms_arrow_pass = self.shoot_random_rooms(rooms_arrow_pass, room_prev)
                wrong_room = True
                break

            rooms_arrow_pass.append(room_target)
            room_prev = room_target

        return rooms_arrow_pass, wrong_room


    @check_active_user
    def shoot(self, input_seq):
        '''Управление полетом стрелы'''
        player_room = self.game_objects['player_history'][-1]
        wampus_room = self.game_objects['wampus'][0]

        rooms_arrow = v.find_numbers(input_seq)
        if len(rooms_arrow) == 5:

            if self.game_user['arrows'] > 0:

                self.game_user['arrows'] -= 1
                rooms_arrow_pass, wrong_room = self.shoot_check_rooms(rooms_arrow, player_room)

                if wampus_room in rooms_arrow_pass:
                    return self.replics.shoot_wampus_killed(rooms_arrow_pass,wampus_room)

                if player_room in rooms_arrow_pass:
                    self.game_user['lives'] -=1
                    return self.replics.shoot_player_killed(rooms_arrow_pass,player_room)

                response = self.replics.shoot_process(rooms_arrow_pass, wrong_room, self.game_user['arrows'])

            else:

                self.game_user['lives'] -=1
                response = self.replics.arrows_over()

        else:
            response = self.replics.shoot_wrong_input()


        return response


    def help(self, input_seq):
        '''Выход из игры - сброс мира'''

        r = '''В игре доступны команды:
                Переход в комнату - надо указать номер смежной комнаты.
                Выстрел из лука - надо указать номера 5 комнат через которые пролетит стрела.
                Состояние - чтобы узнать сколько у вас стрел.'''
        return r


    def health(self, input_seq):
        ''''''

        r = '''У вас осталось {} стрел'''.format(self.game_user['arrows'])

        return r


    def exit(self, input_seq):
        '''Выход из игры - сброс мира'''

        self.game_objects = {}
        self.game_spacegame_rooms = {}
        self.game_user = {}

        return 'Вы вышли из игры'
