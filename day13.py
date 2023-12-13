def get_pattern_value(pattern):
    height = len(pattern)
    width = len(pattern[0])

    for i in range(1, width):
        left_part_rev = [pattern[k][:i][::-1] for k in range(height)]
        right_part = [pattern[k][i:] for k in range(height)]
        reflection_cnt = min(len(left_part_rev[0]), len(right_part[0]))

        if [x[:reflection_cnt] for x in left_part_rev] == [x[:reflection_cnt] for x in right_part]:
            return i

    for j in range(1, height):
        upper_part_rev = pattern[:j][::-1]
        lower_part = pattern[j:]
        reflection_cnt = min(len(upper_part_rev), len(lower_part))

        if upper_part_rev[:reflection_cnt] == lower_part[:reflection_cnt]:
            return 100 * j


def part1(task_input):
    patterns = [[list(row) for row in pattern.split('\n')] for pattern in task_input.split('\n\n')]
    result = 0
    for pattern in patterns:
        result += get_pattern_value(pattern)
    return result


def part2(task_input):
    pass
