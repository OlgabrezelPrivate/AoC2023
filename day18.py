def extend_ground(ground, position, direction, steps):
    match direction:
        case "U":
            width = len(ground[0])
            cur_row = position[1]
            new_row = cur_row - steps
            while new_row < 0:
                ground.insert(0, ['.'] * width)
                new_row += 1
                cur_row += 1
                position = (position[0], cur_row)
        case "D":
            width = len(ground[0])
            cur_row = position[1]
            new_row = cur_row + steps
            while new_row >= len(ground):
                ground.append(['.'] * width)
        case "L":
            cur_col = position[0]
            new_col = cur_col - steps
            while new_col < 0:
                for i in range(len(ground)):
                    ground[i].insert(0, '.')
                new_col += 1
                cur_col += 1
                position = (cur_col, position[1])
        case "R":
            cur_col = position[0]
            new_col = cur_col + steps
            while new_col >= len(ground[0]):
                for i in range(len(ground)):
                    ground[i].append('.')
    return position


def dig_edge(instructions):
    ground = [['#']]
    position = (0, 0)
    for direction, steps, color in instructions:
        steps = int(steps)
        position = extend_ground(ground, position, direction, steps)
        for i in range(steps):
            match direction:
                case "U":
                    position = (position[0], position[1] - 1)
                case "D":
                    position = (position[0], position[1] + 1)
                case "R":
                    position = (position[0] + 1, position[1])
                case "L":
                    position = (position[0] - 1, position[1])
            ground[position[1]][position[0]] = '#'
    return ground


def dig_interior(ground):
    height = len(ground)
    width = len(ground[0])
    for j in range(height):
        inside = False
        i = 0
        while i < width:
            if ground[j][i] == '#':
                edge_from_top = (j > 0) and (ground[j - 1][i] == '#')
                while (i + 1 < width) and (ground[j][i + 1] == '#'):
                    i += 1
                edge_to_bottom = (j < height - 1) and (ground[j + 1][i] == '#')
                if edge_from_top == edge_to_bottom:
                    inside = not inside
            elif inside:
                ground[j][i] = 'i'  # mark the tile as "inside" the edge (not an edge) so the rest of the algorithm works.

            i += 1

    for j in range(height):
        for i in range(width):
            if ground[j][i] == 'i':
                ground[j][i] = '#'


def print_ground(ground):
    print('\n'.join([''.join(x) for x in ground]) + '\n')


def part1(task_input):
    instructions = [tuple(x.split(' ')) for x in task_input.split('\n')]
    ground = dig_edge(instructions)
    dig_interior(ground)
    return sum(row.count('#') for row in ground)


def part2(task_input):
    pass
