def part1(task_input):
    series = [[int(x) for x in y.split(' ')] for y in task_input.split('\n')]
    result = 0

    for s in series:
        cur = s
        extra = [s]
        while any(x for x in cur if x != 0):
            nxt = []
            for i in range(len(cur) - 1):
                nxt.append(cur[i + 1] - cur[i])
            extra.append(nxt)
            cur = nxt

        extra[-1].append(0)
        for i in range(len(extra) - 2, -1, -1):
            extra[i].append(extra[i][-1] + extra[i+1][-1])

        result += extra[0][-1]
    return result


def part2(task_input):
    pass
