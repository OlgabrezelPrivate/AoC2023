def get_games(task_input):
    lines = task_input.split('\n')
    shown = []
    for line in lines:
        info = line.split(': ')
        game_no = int(info[0][info[0].index(' ')+1:])

        games = []
        game_info = info[1].split('; ')
        for g in game_info:
            dice = {'r': 0, 'g': 0, 'b': 0}
            colors = g.split(', ')
            for c in colors:
                dice_info = c.split(' ')
                dice_cnt = int(dice_info[0])
                dice_color = dice_info[1][0]
                dice[dice_color] = dice_cnt

            games.append(dice)
        shown.append((game_no, games))
    return shown


def part1(task_input):
    games = get_games(task_input)
    R, G, B = 12, 13, 14
    possible_sum = 0

    for g in games:
        game_no = g[0]
        rolls = g[1]
        for roll in rolls:
            if roll['r'] > R or roll['g'] > G or roll['b'] > B:
                break
        else:  # We never hit break, so all rolls in this game were possible
            possible_sum += game_no

    return possible_sum


def part2(task_input):
    pass
