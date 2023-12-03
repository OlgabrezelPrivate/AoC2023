def get_num_place(line, idx):
    i = idx
    j = idx
    while (i > 0) and (line[i - 1].isdigit()):
        i -= 1
    while (j < len(line) - 1) and (line[j + 1].isdigit()):
        j += 1

    return i, j


def part1(task_input):
    lines = task_input.split('\n')

    number_places = set()
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            c = line[x]
            if (not c.isdigit()) and (c != '.'):
                for i in range(-1, 2):
                    if 0 <= y + i < len(lines):
                        for j in range(-1, 2):
                            if 0 <= x + j < len(lines[y + i]):
                                if lines[y + i][x + j].isdigit():
                                    number_places.add((y + i, get_num_place(lines[y + i], x + j)))

    return sum(int(lines[line_idx][start:stop + 1]) for line_idx, (start, stop) in number_places)


def part2(task_input):
    pass
