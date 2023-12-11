def get_universe_expansion(task_input):
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

    return lines, insert_lines, insert_cols


def expand_universe_part1(task_input):
    lines, insert_lines, insert_cols = get_universe_expansion(task_input)
    width = len(lines[0])

    for i in insert_lines[::-1]:
        lines.insert(i, list('.' * width))

    height = len(lines)
    for j in insert_cols[::-1]:
        for i in range(height):
            lines[i].insert(j, '.')

    return lines


def part1(task_input):
    universe = expand_universe_part1(task_input)
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
    universe, insert_lines, insert_cols = get_universe_expansion(task_input)
    height = len(universe)
    width = len(universe[0])
    expansion_factor = 1000000
    distance_sum = 0

    galaxies = [(j, i) for j in range(height) for i in range(width) if universe[j][i] == '#']
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 < g2:
                expansions = 0
                smaller_j = min(g1[0], g2[0])
                higher_j = max(g1[0], g2[0])
                expansions += len([j for j in insert_lines if smaller_j <= j <= higher_j])

                smaller_i = min(g1[1], g2[1])
                higher_i = max(g1[1], g2[1])
                expansions += len([i for i in insert_cols if smaller_i <= i <= higher_i])

                distance_sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + (expansion_factor - 1) * expansions

    return distance_sum
