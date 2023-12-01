def part1(task_input):
    lines = task_input.split('\n')
    digits = [list(filter(lambda x: x.isdigit(), line)) for line in lines]  # list of string of digits only for each row
    return sum(10 * int(d[0]) + int(d[-1]) for d in digits if d)


def part2(task_input):
    pass
