def get_pattern_values(pattern):
    height = len(pattern)
    width = len(pattern[0])
    results = []

    for i in range(1, width):
        left_part_rev = [pattern[k][:i][::-1] for k in range(height)]
        right_part = [pattern[k][i:] for k in range(height)]
        reflection_cnt = min(len(left_part_rev[0]), len(right_part[0]))

        if [x[:reflection_cnt] for x in left_part_rev] == [x[:reflection_cnt] for x in right_part]:
            results.append(i)

    for j in range(1, height):
        upper_part_rev = pattern[:j][::-1]
        lower_part = pattern[j:]
        reflection_cnt = min(len(upper_part_rev), len(lower_part))

        if upper_part_rev[:reflection_cnt] == lower_part[:reflection_cnt]:
            results.append(100 * j)

    return results


def part1(task_input):
    patterns = [[list(row) for row in pattern.split('\n')] for pattern in task_input.split('\n\n')]
    result = 0
    for pattern in patterns:
        result += get_pattern_values(pattern)[0]  # There is always exactly one reflection line for part 1
    return result


def part2(task_input):
    patterns = [[list(row) for row in pattern.split('\n')] for pattern in task_input.split('\n\n')]

    result = 0
    for pattern in patterns:
        height = len(pattern)
        width = len(pattern[0])
        found = False

        orig_value = get_pattern_values(pattern)[0]  # The one original reflection line value

        for j in range(height):
            for i in range(width):
                changed = [row.copy() for row in pattern]
                changed[j][i] = '.' if changed[j][i] == '#' else '#'
                changed_val = get_pattern_values(changed)  # There might be zero, or even two reflection lines, since
                new_val = [x for x in changed_val if x != orig_value]  # the original one might stay intact.
                if new_val:
                    result += new_val[0]
                    found = True
                    break

            if found:
                break

    return result
