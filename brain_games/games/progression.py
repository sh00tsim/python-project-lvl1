import prompt
from random import randint
from brain_games.implementer import defeat_message
from brain_games.implementer import victory_message


def create_progression(item, range_row, len_row):
    row = [item]
    while len(row) < len_row:
        row.append(item + range_row)
        item += range_row
    return row


def quest_progression(item, range_row, len_row, quest_item):
    quest = create_progression(item, range_row, len_row)
    item = quest[quest_item]
    quest[quest_item] = '..'
    return [item, quest]


def correct_answer(item, range_row, len_row, quest_item):
    answer = quest_progression(item, range_row, len_row, quest_item)
    return answer[0]


def user_answer(item, range_row, len_row, quest_item):
    progression = quest_progression(item, range_row, len_row, quest_item)
    print('Question: ' + ' '.join(str(item) for item in progression[1]))
    global answer
    answer = prompt.string('Your answer: ')
    return answer


def progression():
    round_game = 0
    print('What number is missing in the progression?')
    while round_game < 3:
        item = randint(0, 100)
        range_row = randint(1, 100)
        len_row = randint(5, 10)
        quest_item = randint(0, len_row - 1)
        answer_correct = correct_answer(item, range_row, len_row, quest_item)
        answer_user = user_answer(item, range_row, len_row, quest_item)
        if str(answer_correct) == answer_user:
            print('Correct!')
            round_game += 1
        else:
            return print(defeat_message(answer, answer_correct))
    return print(victory_message())
