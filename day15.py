def hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val


def part1(task_input):
    steps = task_input.split(',')
    return sum(hash(s) for s in steps)


def part2(task_input):
    pass
