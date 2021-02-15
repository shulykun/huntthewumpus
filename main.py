
import vectorizer as v
from game_actions import Actions

g_actions = Actions()

content_map = [
    {
        'index':'заново перезапуск перезагрузка рестарт',
        'function':g_actions.restart
    },
    {
        'index':'перейти комната переход идти иду',
        'function':g_actions.move_room
    },
    {
        'index':'стрелять стрела стреляю запускать_стрела',
        'function':g_actions.shoot
    },
    {
        'index':'выход',
        'function':g_actions.exit
    },
    {
        'index':'старт',
        'function':g_actions.start
    },
    {
        'index':'помощь команды справка',
        'function':g_actions.help
    },
    {
        'index':'состояние',
        'function':g_actions.health
    }
]


def console_dialogue():

    print('HUNT THE WUMPUS')
    for r in g_actions.start('').split('.'):
        print(r.strip())

    while True:

        input_sequense = input()

        content_answer = v.select_answer(input_sequense, content_map)
        if content_answer:
            choose_function = content_answer['function']
        else:
            choose_function= g_actions.not_found
        response = choose_function(input_sequense)

        print('---')
        for r in response.split('.'):
            print(r.strip())
        print('---')


if __name__ == "__main__":
    console_dialogue()
