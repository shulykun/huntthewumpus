class Replics():

    def start_game(self, start_room, near_rooms):

        r = '''Вы попали в лабиринт где обитает Вампус - большой и опасный монстр.
                Единственный способ выбраться отсюда и выжить - найти Вампуса и застрелить его.
                Сейчас вы находитесь в комнате {}. Вы можете перейти в смежные комнаты: {}
            '''.format(start_room, ', '.join(map(str,near_rooms)))

        return r


    def restart_game(self, start_room, near_rooms):

        r = '''Перезапускаем игру! Вы снова в лабиринте Вампуса и должны сразиться с ним, чтобы выйти.
                Сейчас вы находитесь в комнате {}. Вы можете перейти в смежные комнаты: {}
            '''.format(start_room, ', '.join(map(str, near_rooms)))

        return r


    def game_over(self):

        r = '''Вы проиграли :-( Напишите «старт», чтобы начать новую игру'''
        return r


    def move_room_empty(self, room_to, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Вы в комнате {}. Открыт проход в комнаты {}'''.format(room_to, rooms_connect)
        return r


    def move_room_bats(self):

        r = '''Летучие мыши нападают на вас и уносят в неизвестном направлении..'''
        return r


    def move_room_bats_near(self, room_to, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Вы в комнате {}. Где-то рядом слышен шум.Соседние комнаты {}'''\
        .format(room_to, rooms_connect)
        return r


    def move_room_holes(self, room_to, rooms_connect):

        r = 'Роковая ошибка. Вы провалились в яму в комнате {}. Увы, игра окончена :('.format(room_to)
        # r = '''Вы в комнате {}. О, нет, тут яма!'''.format(room_to)
        return r


    def move_room_holes_near(self, room_to, rooms_connect):

        rooms_connect =', '.join(map(str,rooms_connect))

        r = '''Вы в комнате {}. Вы чувствуете сквозняк, похоже, в соседней комнате яма.
        Будьте осторожны. Открыт проход в комнаты {}'''.format(room_to, rooms_connect)
        return r


    def move_room_wampus(self, room_to, rooms_connect):

        r = '''Вы попали в комнату {} и угодили прямо в пасть Вампуса! Игра окончена :-('''.format(room_to)
        return r


    def move_room_wampus_near(self, room_to, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Вы в комнате {}. Откуда-то раздается отвратительное зловоние.
        Похоже, монстр в соседней комнате. Открыт доступ в комнаты {}'''\
        .format(room_to, rooms_connect)
        return r


    def move_room_close(self, room_from, room_to, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Из комнаты {} нет доступа в {}. Выберите из соседних комнат: {}'''\
            .format(room_from, room_to, rooms_connect)
        return r


    def move_room_same(self, room_from, rooms_connect):

        rooms_connect = ', '.join(map(str,rooms_connect))
        r = '''Вы ходите по кругу в комнате {}. Попробуйте выйти в соседние комнаты: {}'''\
            .format(room_from,rooms_connect)

        return r


    def move_wrong_input(self):

        return '''Введите корректное количество комнат'''


    def shoot_process(self, room_numbers, wrong_room, arrows_count):

        room_numbers = ', '.join(map(str,room_numbers))

        if wrong_room:
            response = '''Выстрел! Стрела сбилась с пути! Она пролетает через комнаты {}. Мимо!'''.format(room_numbers)
        else:
            response = '''Выстрел! Стрела нацелена в комнаты {}. Мимо!'''.format(room_numbers)

        if arrows_count == 0:
            response_arr_count = "У вас не осталось стрел. Это поражение :-("
        else:
            response_arr_count = 'Осталось стрел: {}.'.format(arrows_count)

        return '{} {}'.format(response,response_arr_count)


    def shoot_wrong_input(self):

        return '''Чтобы выстрелить, укажите 5 комнат'''


    def shoot_wrong_room(self, room_numbers, room_target, room_prev, arrows_count):

        room_numbers = ', '.join(map(str,room_numbers))

        a = '''Выстрел! Стрела нацелена в комнаты {}.'''.format(room_numbers)
        b = "Ошибка! Комната {} не связана с {}. Стрела".format(room_target, room_prev)

        if arrows_count == 0:
            response_arr_count = "У вас не осталось стрел. Это поражение :-("
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
        b = "Стрела срикошетила и убивает Вас в комнате {}".format(room_target)

        return '{} {}'.format(a,b)


    def  arrows_over(self):

        return '''Увы, ваши стрелы закончились. Вы обречены. Напишите «старт» для новой попытки.'''


    def not_found(self):

        return '''Я не могу понять этот запрос. Попробуйте набрать: старт, переход в комнату, стрелять.'''


    def help(self):
        r = '''В игре доступны команды:
                Переход в комнату - надо указать номер смежной комнаты.
                Выстрел из лука - надо указать номера 5 комнат через которые пролетит стрела.
                Состояние - чтобы узнать сколько у вас стрел.'''
        return r
