def part1(task_input):
    lines = task_input.split('\n')
    cards = []
    for line in lines:
        parts = line.split(': ')
        card_no = int(parts[0][parts[0].index(' ') + 1:])
        numbers = parts[1].split(' | ')
        winning_nums = {int(x) for x in numbers[0].split(' ') if x}
        have_nums = {int(x) for x in numbers[1].split(' ') if x}
        cards.append((card_no, winning_nums, have_nums))

    points = 0

    for c in cards:
        won = c[1].intersection(c[2])
        points += 0 if len(won) == 0 else int(2 ** (len(won) - 1))

    return points


def part2(task_input):
    lines = task_input.split('\n')
    card_count = {x: 1 for x in range(1, len(lines) + 1)}

    for line in lines:
        parts = line.split(': ')
        card_no = int(parts[0][parts[0].index(' ') + 1:])
        numbers = parts[1].split(' | ')
        winning_nums = {int(x) for x in numbers[0].split(' ') if x}
        have_nums = {int(x) for x in numbers[1].split(' ') if x}
        matching = len(winning_nums.intersection(have_nums))
        for i in range(matching):
            card_count[card_no + 1 + i] += card_count[card_no]

    return sum(card_count.values())
