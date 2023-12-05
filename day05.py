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


def intersect_ranges(range1, range2):
    """Returns a new range which is the intersection of range1 and range2, and
    a list of ranges that form the parts of range1 that don't intersect range2"""
    start1, len1 = range1
    start2, len2 = range2

    # No intersection
    if (start1 + len1 <= start2) or (start2 + len2 <= start1):
        return None

    # Range 2 is enclosed by range 1
    if (start1 <= start2) and (start1 + len1 >= start2 + len2):
        rests = []
        if start1 < start2:
            rests.append((start1, start2 - start1))
        if start1 + len1 > start2 + len2:
            rests.append((start2 + len2, start1 + len1 - start2 - len2))
        return start2, len2, rests

    # Range 1 is enclosed by range 2
    if (start2 <= start1) and (start2 + len2 >= start1 + len1):
        return start1, len1, []

    # intersect at the left side of range 2
    if (start1 < start2) and (start2 < start1 + len1 <= start2 + len2):
        return start2, start1 + len1 - start2, [(start1, start2 - start1)]

    # intersect at the right side of range 2
    if (start2 < start1) and (start1 < start2 + len2 <= start1 + len1):
        return start1, start2 + len2 - start1, [(start2 + len2, start1 + len1 - start2 - len2)]

    raise Exception('No intersection case applied')


def part2(task_input):
    seed_raw, maps = parse_input(task_input)
    value_ranges = []
    for i in range(0, len(seed_raw), 2):
        value_ranges.append((seed_raw[i], seed_raw[i + 1]))

    new_value_ranges = []

    for mapping in maps:
        while len(value_ranges):  # As long as any source hasn't been mapped to its destination yet
            value_range = value_ranges.pop(0)
            for (dest_start, src_start, range_len) in mapping:
                intersect = intersect_ranges(value_range, (src_start, range_len))
                if intersect:  # There is an intersection - the intersecting part is mapped to the destination, the rest is
                    o_start, o_len, value_range_rests = intersect                        # kept since it could still intersect
                    new_value_ranges.append((o_start + dest_start - src_start, o_len))   # with another entry of this mapping
                    value_ranges += value_range_rests
                    break
            else:
                new_value_ranges.append(value_range)  # No entry of the mapping intersected - map same numbers to destination

        value_ranges = new_value_ranges  # Previous destination becomes new source
        new_value_ranges = []

    return min(v[0] for v in value_ranges)
