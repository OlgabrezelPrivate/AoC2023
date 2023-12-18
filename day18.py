def color_to_instruction(color):
    match color[-2]:
        case '0':
            direction = 'R'
        case '1':
            direction = 'D'
        case '2':
            direction = 'L'
        case '3':
            direction = 'U'

    steps = int(color[2:-2], 16)
    return direction, steps


def get_edges(instructions):
    position = (0, 0)
    edges = []
    for direction, steps in instructions:
        match direction:
            case "U":
                stop = (position[0], position[1] - steps)
            case "D":
                stop = (position[0], position[1] + steps)
            case "R":
                stop = (position[0] + steps, position[1])
            case "L":
                stop = (position[0] - steps, position[1])
        edges.append((min(position, stop), max(position, stop)))
        position = stop
    return edges


def get_row_hole_count(edges, row):
    horizontal_edges = sorted([e for e in edges if e[0][1] == e[1][1] == row])
    row_hole_count = sum(e[1][0] - e[0][0] - 1 for e in horizontal_edges)

    vertical_edges = sorted([e for e in edges if (e[0][0] == e[1][0]) and (e[0][1] <= row <= e[1][1])], key=lambda e: e[0][0])
    iterator = iter(vertical_edges)

    last_x = None
    for e in iterator:
        if (e[0][1] == row) or (e[1][1] == row):  # this is the START or END of a vertical edge.
            e2 = next(iterator)                   # next vertical edge MUST also start or end in the same row. Get it!
            if (e[0][1] == e2[1][1]) or (e[1][1] == e2[0][1]):  # e2 goes the opposite direction than e - toggle "inside" mode
                if last_x is None:
                    last_x = e2[0][0]
                    row_hole_count += 2  # 2 holes for the 2 edge corners
                else:
                    row_hole_count += e[0][0] - last_x + 1
                    last_x = None
            else:  # e2 goes the same direction as e - do not toggle "inside" mode but do count the tiles between last_x and e.
                row_hole_count += 2  # 2 holes for the 2 edge corners
                if last_x is not None:
                    row_hole_count += e[0][0] - last_x - 1  # count everything in between (-1 because corners already counted).
                    last_x = e2[0][0]
        else:                   # This is NOT start or end of a vertical row. Much easier.
            if last_x is None:
                row_hole_count += 1
                last_x = e[0][0]
            else:
                row_hole_count += e[0][0] - last_x
                last_x = None

    return row_hole_count


def get_hole_count(instructions):
    edges = get_edges(instructions)
    hole_count = 0

    top = min([min(e[0][1] for e in edges)] + [min(e[1][1] for e in edges)])
    bottom = max([max(e[0][1] for e in edges)] + [max(e[1][1] for e in edges)])

    important_y_coordinates = sorted({top, bottom}.union({e[0][1] for e in edges}.union({e[1][1] for e in edges})))
    last_y = None

    for y in important_y_coordinates:
        if last_y is not None:
            hole_count += (y - last_y - 1) * get_row_hole_count(edges, y - 1)
        hole_count += get_row_hole_count(edges, y)
        last_y = y

    return hole_count


def part1(task_input):
    instructions_raw = [x.split(' ') for x in task_input.split('\n')]
    instructions = [(ins[0], int(ins[1])) for ins in instructions_raw]
    return get_hole_count(instructions)


def part2(task_input):
    instructions_raw = [x.split(' ') for x in task_input.split('\n')]
    instructions = [color_to_instruction(ins[2]) for ins in instructions_raw]
    return get_hole_count(instructions)
