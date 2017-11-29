def score(game):
    result = 0
    frame = 1
    first_roll = True
    for roll in range(len(game)):
        if frame < 10:
            if game[roll] == '/':
                result = add_spare_result(result, roll, game, last)
            elif game[roll] == 'X' or game[roll] == 'x':
                result = add_strike_result(result, roll, game)
            else:
                result += get_value(game[roll])
                last = get_value(game[roll])
        else:
            result += get_value(game[roll])
        if not first_roll:
            frame += 1
            first_roll = True
        else:
            first_roll = False
        if game[roll] == 'X' or game[roll] == 'x':
            first_roll = True
            frame += 1
    return result

def add_spare_result(result, roll, game, last):
    result += get_value(game[roll]) - last + get_value(game[roll + 1])
    return result

def add_strike_result(result, roll, game):
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

score("------------------X2/")