def parse_input(task_input):
    times, distances = task_input.split('\n')
    times = [int(x) for x in times.split(' ')[1:] if x]
    distances = [int(x) for x in distances.split(' ')[1:] if x]
    return [(times[i], distances[i]) for i in range(len(times))]


def part1(task_input):
    races = parse_input(task_input)
    prod = 1
    for time, distance in races:
        ways = 0
        for speed in range(time + 1):
            travelled = speed * (time - speed)
            if travelled > distance:
                ways += 1
        prod *= ways
    return prod


def part2(task_input):
    return part1(task_input.replace(' ', '').replace(':', ': '))
