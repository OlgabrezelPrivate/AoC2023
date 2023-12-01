def part1(task_input):
    lines = task_input.split('\n')
    digits = [list(filter(lambda x: x.isdigit(), line)) for line in lines]  # list of string of digits only for each row
    return sum(10 * int(d[0]) + int(d[-1]) for d in digits if d)


def part2(task_input):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(words)):
        w = words[i]
        # keep the first and last letter of each digit to allow overlaps like "onEight". These are at most one letter long.
        task_input = task_input.replace(w, f'{w[0]}{i + 1}{w[-1]}')

    return part1(task_input)
