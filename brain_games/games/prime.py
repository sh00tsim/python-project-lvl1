import prompt
from random import randint
from brain_games.implementer import defeat_message
from brain_games.implementer import victory_message


def correct_answer(number):
    set_prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                        53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for item in set_prime_number:
        if number == item:
            return 'yes'
    return 'no'


def user_answer(number):
    print('Question: {}'.format(number))
    global answer
    answer = prompt.string('Your answer: ')
    return answer


def prime_number():
    round_game = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while round_game < 3:
        number = randint(0, 100)
        if correct_answer(number) == user_answer(number):
            print('Correct!')
            round_game += 1
        else:
            return print(defeat_message(answer, correct_answer(number)))
    return print(victory_message())
