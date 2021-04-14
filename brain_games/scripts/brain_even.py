#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user


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
            return print("'{}' is wrong answer ;(. Correct answer was '{}.\nLet's try again!".format(user_answer, is_even))
    return print('Congratulations!')


def main():
    welcome_user()
    even_number()


if __name__ == '__main__':
    main()
