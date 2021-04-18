import prompt
from random import randint
from brain_games.implementer import defeat_message
from brain_games.implementer import victory_message


def gcd(number_one, number_two):
    number_one = abs(number_one)
    number_two = abs(number_two)
    while number_one != 0:
        transition = number_two % number_one
        number_two = number_one
        number_one = transition
    return number_two


def correct_answer(number_one, number_two):
    return gcd(number_one, number_two)


def user_answer(number_one, number_two):
    print('Question: GCD({}, {})'.format(number_one, number_two))
    global answer
    answer = prompt.string('Your answer: ')
    return answer


def gcd_numbers():
    round_game = 0
    print('Find the greatest common divisor of given numbers.')
    while round_game < 3:
        number_one = randint(0, 100)
        number_two = randint(0, 100)
        answer_correct = correct_answer(number_one, number_two)
        answer_user = user_answer(number_one, number_two)
        if str(answer_correct) == answer_user:
            print('Correct!')
            round_game += 1
        else:
            return print(defeat_message(answer, answer_correct))
    return print(victory_message())
