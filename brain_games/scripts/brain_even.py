#!/usr/bin/env python3

import prompt
from random import randint


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def is_even_number(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def answer_user(number):
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    return answer


def even_number():
    count_correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_correct_answers < 3:
        number = randint(1, 99)
        is_even = is_even_number(number)
        user_answer = answer_user(number)
        if is_even == user_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            defeat_message = "'{}' is wrong answer ;(. ".format(user_answer)
            defeat_message += "Correct anwes was '{}'.".format(is_even)
            defeat_message += "\nLet's try again, {}!".format(name)
            return print(defeat_message)
    return print('Congratulations, {}!'.format(name))


def main():
    welcome_user()
    even_number()


if __name__ == '__main__':
    main()
