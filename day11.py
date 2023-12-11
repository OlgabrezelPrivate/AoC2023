def expand_universe(task_input):
    lines = [list(x) for x in task_input.split('\n')]
    height = len(lines)
    width = len(lines[0])

    insert_lines = []
    insert_cols = []

    for i in range(height):
        if '#' not in lines[i]:
            insert_lines.append(i)
    for j in range(width):
        if '#' not in [lines[k][j] for k in range(height)]:
            insert_cols.append(j)

    for i in insert_lines[::-1]:
        lines.insert(i, list('.' * width))

    height = len(lines)
    for j in insert_cols[::-1]:
        for i in range(height):
            lines[i].insert(j, '.')

    return lines


def part1(task_input):
    universe = expand_universe(task_input)
    height = len(universe)
    width = len(universe[0])

    galaxies = [(j, i) for j in range(height) for i in range(width) if universe[j][i] == '#']
    distance_sum = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 > g2:
                distance_sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return distance_sum


def part2(task_input):
    pass
