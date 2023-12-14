def tilt_north(field):
    height = len(field)
    width = len(field[0])
    changed = True
    while changed:
        changed = False
        for j in range(height - 1):
            for i in range(width):
                if (field[j][i] == '.') and (field[j+1][i] == 'O'):
                    changed = True
                    field[j][i] = 'O'
                    field[j+1][i] = '.'


def load_on_north_axis(field):
    height = len(field)
    width = len(field[0])
    return sum(height - j for j in range(height) for i in range(width) if field[j][i] == 'O')


def part1(task_input):
    field = [list(row) for row in task_input.split('\n')]
    tilt_north(field)
    return load_on_north_axis(field)


def part2(task_input):
    pass
