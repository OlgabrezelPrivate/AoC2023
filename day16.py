def get_energized_tile_count(grid, initial_light):
    LIGHTS = set()
    height = len(grid)
    width = len(grid[0])

    lights = {initial_light}
    energized = {(initial_light[0], initial_light[1])}
    while lights:
        lights_tpl = tuple(sorted(lights))
        if lights_tpl in LIGHTS:
            break
        LIGHTS.add(lights_tpl)

        new_lights = set()
        for light in lights:
            j = light[0]
            i = light[1]
            direction = light[2]
            going = [direction]

            match grid[j][i]:
                case '-':
                    if direction in ['U', 'D']:
                        going = ['L', 'R']
                case '|':
                    if direction in ['L', 'R']:
                        going = ['U', 'D']
                case '/':
                    match direction:
                        case 'L':
                            going = ['D']
                        case 'R':
                            going = ['U']
                        case 'U':
                            going = ['R']
                        case 'D':
                            going = ['L']
                case '\\':
                    match direction:
                        case 'L':
                            going = ['U']
                        case 'R':
                            going = ['D']
                        case 'U':
                            going = ['L']
                        case 'D':
                            going = ['R']

            for new_direction in going:
                match new_direction:
                    case 'L':
                        if i > 0:
                            new_lights.add((j, i - 1, 'L'))
                    case 'R':
                        if i < width - 1:
                            new_lights.add((j, i + 1, 'R'))
                    case 'U':
                        if j > 0:
                            new_lights.add((j - 1, i, 'U'))
                    case 'D':
                        if j < height - 1:
                            new_lights.add((j + 1, i, 'D'))

        for new_light in new_lights:
            energized.add((new_light[0], new_light[1]))

        lights = new_lights

    return len(energized)


def part1(task_input):
    grid = [list(row) for row in task_input.split('\n')]
    return get_energized_tile_count(grid, (0, 0, 'R'))


def part2(task_input):
    pass
