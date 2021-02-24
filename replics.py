class Replics():

    def start_game(self):

        r = '''-- HUNT THE WUMPUS --##
                Вы попали в лабиринт, где обитает Вампус - большой и опасный монстр.
                # Единственный способ выбраться отсюда - найти и убить его.#
                Для этого у вас есть лук и 5 волшебных стрел, которые летят через комнаты по указаному вами пути.#
                Будьте осторожны: лабиринт таит в себе немало опасностей!##

                -- ОБИТАТЕЛИ ЛАБИРИНТА --#

                Летучие мыши - могут напасть и перенести в любую случайную комнату. ##
                Блуждающие ямы - внезапно появляются в пещерах лабиринта. Если вы чувствуете сквозняк, берегитесь - яма в соседней комнате. ##
                Подземный тролль - время от времени приходит в лабиринт тайными тропами. Требует сыграть с ним в «камень-ножницы-бумага», может отобрать стрелу или дать подсказку. Его также можно позвать, набрав «тролль»##
                Вампус - монстр, который спит в лабиринте. Его никто не видел, но горе тому, кто наткнется на него в пещере.##
                -- ИГРА НАЧАЛАСЬ! --



            '''

        return r



    def game_over(self):

        r = '''Вы проиграли :-( Напишите «старт», чтобы начать новую игру'''
        return r


    def utils_room_near(self, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Открыт проход в смежные комнаты : {}.'''.format(rooms_connect)
        return r


    def move_room_empty(self, room_to, rooms_connect):

        r = '''Вы в комнате {}. {}'''.format(room_to, self.utils_room_near(rooms_connect))
        return r


    def move_room_bats(self):

        r = '''Летучие мыши нападают на вас и уносят в неизвестном направлении.'''
        return r


    def move_room_holes(self, room_to, rooms_connect):

        r = '''Роковая ошибка. Вы провалились в яму в комнате {}.
        ##--ИГРА ОКОНЧЕНА--# Наберите «рестарт» чтобы начать заново.'''.format(room_to)

        return r


    def move_room_wampus(self, room_to, rooms_connect):

        r = '''Вы попали в комнату {} и угодили прямо в пасть Вампуса! ##
        --ИГРА ОКОНЧЕНА--# Наберите «рестарт» чтобы начать заново.'''.format(room_to)
        return r


    def move_room_bats_near(self, room_to, rooms_connect):

        r = '''Вы в комнате {}. Где-то рядом слышен шум. {}'''\
        .format(room_to, self.utils_room_near(rooms_connect))
        return r


    def move_room_holes_near(self, room_to, rooms_connect):

        r = '''Вы в комнате {}. Вы чувствуете сквозняк, похоже, в соседней комнате яма.#
        Будьте осторожны. {}'''.format(room_to, self.utils_room_near(rooms_connect))
        return r


    def move_room_wampus_near(self, room_to, rooms_connect):

        r = '''Вы в комнате {}. Откуда-то раздается отвратительное зловоние.#
        Похоже, в соседней комнате спит сам Вампус. {}'''\
        .format(room_to, self.utils_room_near(rooms_connect))
        return r


    def move_room_danger_near(self, keys_list, room_to, rooms_connect):

        danger_name = {'wampus_near':'чувствуется зловоние',
        'holes_near':'доносится сквозняк',
        'bats_near':'слышен шум'}

        danger_names = ' и '.join([danger_name[i] for i in keys_list])

        r = '''Вы в комнате {}.  Из соседних комнат {}. Похоже, опасности поджидают со всех сторон. {}'''\
        .format(room_to, danger_names, self.utils_room_near(rooms_connect))

        return r


    def move_room_close(self, room_from, room_to, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Из комнаты {} нет доступа в {}.# Выберите из соседних комнат: {}.'''\
            .format(room_from, room_to, rooms_connect)
        return r


    def move_room_same(self, room_from, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Вы ходите по кругу в комнате {}.# Попробуйте выйти в соседние комнаты: {}.'''\
            .format(room_from,rooms_connect)

        return r


    def move_wrong_input(self):

        return '''Укажите один номер - комнаты, в которую надо перейти.'''


    def shoot_process(self, room_numbers, wrong_room, arrows_count):

        room_numbers = ', '.join(map(str,room_numbers))

        if wrong_room:
            response = '''Выстрел! Стрела сбилась с пути! Она пролетает через комнаты {}.# Мимо!'''.format(room_numbers)
        else:
            response = '''Выстрел! Стрела нацелена в комнаты {}.# Мимо!'''.format(room_numbers)

        if arrows_count == 0:
            response_arr_count = "У вас не осталось стрел.# Это поражение :-("
        else:
            response_arr_count = 'Осталось стрел: {}.'.format(arrows_count)

        return '{} {}'.format(response,response_arr_count)


    def shoot_wrong_input(self):

        return '''Чтобы выстрелить, укажите номера 5 комнат по порядку.
        # Если вы ошибетесь, стрела срикошетит в случайную комнату и может убить вас.'''


    def shoot_wrong_room(self, room_numbers, room_target, room_prev, arrows_count):

        room_numbers = ', '.join(map(str,room_numbers))

        a = '''Выстрел! Стрела нацелена в комнаты {}.'''.format(room_numbers)
        b = "Ошибка! Комната {} не связана с {}.# Стрела".format(room_target, room_prev)

        if arrows_count == 0:
            response_arr_count = '''У вас не осталось стрел. Это поражение :-(
            ##--ИГРА ОКОНЧЕНА--# Наберите «рестарт» чтобы начать заново.'''
        else:
            response_arr_count = 'Осталось стрел: {}'.format(arrows_count)

        return '{} {} {}'.format(a,b, response_arr_count)


    def shoot_wampus_killed(self,room_numbers,room_target):

        room_numbers = ', '.join(map(str,room_numbers))

        a = "Выстрел! Стрела нацелена в комнаты {}.".format(room_numbers)
        b = "Это победа! Стрела поразила Вампуса в комнате {}.".format(room_target)

        return '{} {}'.format(a,b)


    def shoot_player_killed(self,room_numbers,room_target):

        room_numbers = ', '.join(map(str,room_numbers))

        a = "Выстрел! Стрела нацелена в комнаты {}.".format(room_numbers)
        b = '''Стрела срикошетила и убивает Вас в комнате {}.

        ##--ИГРА ОКОНЧЕНА--# Наберите «рестарт» чтобы начать заново.'''.format(room_target)

        return '{} {}'.format(a,b)


    def arrows_over(self):

        return '''Увы, ваши стрелы закончились. Вы обречены. ##
        --ИГРА ОКОНЧЕНА--# Наберите «рестарт» чтобы начать заново.'''


    def not_found(self):

        return '''Я не могу понять этот запрос. Попробуйте набрать: «старт», «идти», «стрелять», «помощь».'''


    def troll_talk(self):

        return '''Откуда-то в пещере появляется тролль.
        # - Хе-хе. Я вижу, ты все еще блуждаешь. Я давно за тобой наблюдаю.
        # Сыграй в мою любимую игру или я отберу у тебя одну стрелу. # Отвечай: да или нет.'''


    def troll_start_game(self):

        return '''- Начинаем игру. Будем играть три раза. Ты первый. Камень, ножницы или бумага?»'''


    def troll_deny_game(self, arrows_num):

        return '''- Ты отказался играть со мной, значит стрела остается у меня. Всего хорошего!
        # У вас осталось стрел: {}'''.format(arrows_num)


    def troll_re_game(self):

        return '''- Ты отказался играть со мной, значит стрела остается у меня. Всего хорошего!
        # У вас осталось стрел: {}'''.format(arrows_num)


    def troll_comment_game(self, result, troll_var):
        if result == 1:
            return '''- {}! # Ай, не повезло :-( # Говори дальше!'''.format(troll_var)
        else:
            return '''- {}! # Этот раунд я выиграл! # Говори дальше!'''.format(troll_var)

    def troll_loose_game(self, arrows_num):

        return '''- Аххаха! Ты проиграл! Я забираю твою стрелу. Пока!
        # И тролль исчез из пещеры.## У вас осталось стрел: {}'''.format(arrows_num)


    def troll_win_game(self, object, room):

        object_names = {'wampus':'Вампус',
        'holes':'Смертельная яма',
        'bats':'Стая летучих мышей'}

        return '''- Ты выиграл! Хорошо, я дам тебе подсказку. {} находится в комнате {}.
         # И тролль исчез из пещеры.'''\
            .format(object_names[object],room)


    def help(self):
        r = '''В игре доступны команды:#«Идти» - надо указать номер смежной комнаты.#
                «Стрелять» - надо указать номера 5 комнат, через которые пролетит стрела.#
                «Состояние» - чтобы узнать сколько у вас стрел.'''
        return r
