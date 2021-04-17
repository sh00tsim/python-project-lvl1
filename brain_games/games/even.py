import prompt
from random import randint
from brain_games.implementer import defeat_message
from brain_games.implementer import victory_message


def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def user_answer(number):
    print('Question: {}'.format(number))
    global answer
    answer = prompt.string('Your answer: ')
    return answer


def even_number():
    round_game = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while round_game < 3:
        number = randint(1, 99)
        if correct_answer(number) == user_answer(number):
            print('Correct!')
            round_game += 1
        else:
            return print(defeat_message(answer, correct_answer(number)))
    return print(victory_message())
