def parse_input(task_input):
    categories = task_input.split('\n\n')
    seeds = [int(x) for x in categories[0].split(' ')[1:]]

    maps = []
    for i in range(1, len(categories)):
        cat = categories[i].split('\n')[1:]
        mapping = []
        for line in cat:
            dest_start, src_start, range_len = map(int, line.split(' '))
            mapping.append((dest_start, src_start, range_len))
        maps.append(mapping)

    return seeds, maps


def part1(task_input):
    seeds, maps = parse_input(task_input)
    locations = []

    for seed in seeds:
        value = seed
        for mapping in maps:
            for (dest_start, src_start, range_len) in mapping:
                if src_start <= value < src_start + range_len:
                    value += dest_start - src_start
                    break
        locations.append(value)

    return min(locations)


def part2(task_input):
    pass
