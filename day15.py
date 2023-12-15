def hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val


def part1(task_input):
    steps = task_input.split(',')
    return sum(hash(s) for s in steps)


def put_lenses_in_boxes(steps):
    hashmap = [[] for i in range(256)]
    for step in steps:
        if '=' in step:
            parts = step.split('=')
            label = parts[0]
            value = int(parts[1])
            box = hash(label)
            for i in range(len(hashmap[box])):
                if hashmap[box][i][0] == label:
                    hashmap[box][i] = (label, value)
                    break
            else:
                hashmap[box].append((label, value))

        else:  # string ends with a -
            label = step[:-1]
            box = hash(label)
            for i in range(len(hashmap[box])):
                if hashmap[box][i][0] == label:
                    hashmap[box].pop(i)
                    break
    return hashmap


def focusing_power(hashmap):
    power = 0
    for box in range(len(hashmap)):
        for i in range(len(hashmap[box])):
            power += (box + 1) * (i + 1) * hashmap[box][i][1]
    return power


def part2(task_input):
    steps = task_input.split(',')
    hashmap = put_lenses_in_boxes(steps)
    return focusing_power(hashmap)
