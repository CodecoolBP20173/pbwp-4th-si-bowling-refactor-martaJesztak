def score(game):
    result = 0
    frame = 1
    first_roll = True
    for roll in range(len(game)):
        if frame < 10:
            result = calculate_normal_game_result(game, roll, result)
        else:
            result = calculate_bonus_game_result(game, roll, result)
        frame = frame_check(frame, first_roll, game, roll)
        first_roll = is_next_first_roll(first_roll, game, roll)
    return result


def calculate_normal_game_result(game, roll, result):
    if game[roll] == '/':
        result = add_spare_points_to_total(result, roll, game)
    elif game[roll] == 'X' or game[roll] == 'x':
        result = add_strike_points_to_total(result, roll, game)
    else:
        result += get_value(game[roll])
    return result


def calculate_bonus_game_result(game, roll, result):
    result += get_value(game[roll])
    return result


def is_next_first_roll(first_roll, game, roll):
    if not first_roll:
        is_next_first_roll = True
    else:
        if game[roll] != 'X' or game[roll] != 'x':
            is_next_first_roll = False
    return is_next_first_roll


def frame_check(frame, first_roll, game, roll):
    if not first_roll:
            frame += 1
    else:
        if game[roll] == 'X' or game[roll] == 'x':
            frame += 1
    return frame


def add_spare_points_to_total(result, roll, game):
    result += get_value(game[roll]) - get_value(game[roll-1]) + get_value(game[roll + 1])
    return result


def add_strike_points_to_total(result, roll, game):
    result += get_value(game[roll]) + get_value(game[roll + 1])
    if game[roll + 2] == '/':
        result += get_value(game[roll]) - get_value(game[roll + 1])
    else:
        result += get_value(game[roll + 2])
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

score("1/35XXX458/X3/XX6")