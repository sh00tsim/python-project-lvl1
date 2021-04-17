import prompt
from random import randint
from brain_games.implementer import defeat_message
from brain_games.implementer import victory_message


def correct_answer(var_one, var_two, operor):
    if operor == 1:
        return var_one + var_two
    elif operor == 2:
        return var_one - var_two
    elif operor == 3:
        return var_one * var_two


def user_answer(var_one, var_two, operor):
    if operor == 1:
        print('Question: {} + {}'.format(var_one, var_two))
    elif operor == 2:
        print('Question: {} - {}'.format(var_one, var_two))
    elif operor == 3:
        print('Question: {} * {}'.format(var_one, var_two))
    global answer
    answer = prompt.string('Your answer: ')
    return answer


def calculator():
    round_game = 0
    print('What is the result of the expression?')
    while round_game < 3:
        var_one = randint(1, 99)
        var_two = randint(1, 99)
        operor = randint(1, 3)
        answer_correct = str(correct_answer(var_one, var_two, operor))
        answer_user = user_answer(var_one, var_two, operor)
        if answer_correct == answer_user:
            print('Correct!')
            round_game += 1
        else:
            return print(defeat_message(answer, answer_correct))
    return print(victory_message())
