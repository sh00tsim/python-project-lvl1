import prompt


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def defeat_message(user_answer, correct_answer):
    message = "'{}' is wrong answer ;(. ".format(user_answer)
    message += "Correct anwes was '{}'.".format(correct_answer)
    message += "\nLet's try again, {}!".format(name)
    return message


def victory_message():
    message = 'Congratulations, {}!'.format(name)
    return message
