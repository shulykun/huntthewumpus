
import vectorizer as v
from game_actions import Actions

g_actions = Actions()

content_map = [
    {
        'index':'заново перезапуск перезагрузка рестарт',
        'function':g_actions.start
    },
    {
        'index':'перейти комната пещера переход идти иду',
        'function':g_actions.move_room
    },
    {
        'index':'стрелять стрела стреляю запускать_стрела',
        'function':g_actions.shoot
    },
    {
        'index':'старт',
        'function':g_actions.start
    },
    {
        'index':'помощь команды  help справка как_играть',
        'function':g_actions.help
    },
    {
        'index':'состояние',
        'function':g_actions.health
    },
    {
        'index':'где_я',
        'function':g_actions.move_room_whereami
    },
    {
        'index':'выход',
        'function':g_actions.exit_ask
    },
    {
        'index':'да_exit',
        'function':g_actions.exit_confirm
    },
    {
        'index':'нет_exit',
        'function':g_actions.exit_cancel
    },
    # {
    #     'index':'карта',
    #     'function':g_actions.cheat_code
    # },
    {
        'index':'да_askgame нет_askgame askgame',
        'function':g_actions.troll_start_game
    },
    {
        'index':'startgame',
        'function':g_actions.troll_game_restrict
    },
    {
        'index':'камень_startgame startgame',
        'function':g_actions.troll_game_play
    },
    {
        'index':'ножницы_startgame startgame',
        'function':g_actions.troll_game_play
    },
    {
        'index':'бумага_startgame startgame',
        'function':g_actions.troll_game_play
    },
    {
        'index':'тролль',
        'function':g_actions.troll_talk
    }
]


def console_dialogue():

    stop_word = 'exit'
    response_row = ''

    for r in g_actions.start('').split('#'):
        print(r.strip())

    while response_row != stop_word:

        input_sequense = v.sequense_context(input(),g_actions.game_user['context'])
        content_answer = v.select_answer(input_sequense, content_map)
        if content_answer:
            choose_function = content_answer['function']
        else:
            choose_function= g_actions.not_found

        g_actions.init_troll()
        response = choose_function(input_sequense)


        print('---')
        for r in response.split('#'):
            response_row = r.strip()
            print(response_row)
        print('---')


if __name__ == "__main__":
    console_dialogue()
