def parse_input(task_input):
    lines = task_input.split('\n')
    parts = [x.split(' ') for x in lines]
    springs = [list(p[0]) for p in parts]
    configurations = [[int(x) for x in p[1].split(',')] for p in parts]
    return springs, configurations


def transform_springs(springs):
    """Removes consecutive .'s and makes sure there's a . at the beginning and the end"""
    for i in range(len(springs)):
        j = 0
        while j < len(springs[i]) - 1:
            if springs[i][j] == springs[i][j+1] == '.':
                del springs[i][j]
            else:
                j += 1

        if springs[i][0] != '.':
            springs[i].insert(0, '.')
        if springs[i][-1] != '.':
            springs[i].append('.')


def get_arrangements_count(spring, conf):
    # Rather than searching for the number of configurations of the ?s s.t. the configuration is fulfilled,
    # search for the number of ways to split the spring into substrings that alternatingly represent
    # working and broken groups of segments
    arrangements_count = 0

    if len(conf) == 0:
        return 1 if '#' not in spring else 0
    elif ('#' not in spring) and ('?' not in spring):
        return 0

    max_idx = min(spring.index('#') if '#' in spring else len(spring) - 1,
                  len(spring) - sum(conf))

    for i in range(1, max_idx + 1):
        partspring = spring[i:]          # Remove i points from the start of the spring, at least one
        if '.' in partspring[:conf[0]]:  # The next conf[0] segments are defect. If that's not possible, move on.
            continue

        # Remove the conf[0] defect segments and go on recursively
        arrangements_count += get_arrangements_count(partspring[conf[0]:], conf[1:])

    return arrangements_count


def part1(task_input):
    springs, configurations = parse_input(task_input)
    transform_springs(springs)
    arrangements_count = 0
    for i in range(len(springs)):
        spring = springs[i]
        conf = configurations[i]
        arrangements_count += get_arrangements_count(spring, conf)
    return arrangements_count


def part2(task_input):
    pass
