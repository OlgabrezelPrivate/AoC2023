def get_field_count(grid, start_position, steps):
    height = len(grid)
    width = len(grid[0])
    positions = {start_position}
    for step in range(steps):
        new_positions = set()
        while len(positions):
            x, y = positions.pop()
            if (y > 0) and (grid[y - 1][x] == '.'):
                new_positions.add((x, y - 1))
            if (y < height - 1) and (grid[y + 1][x] == '.'):
                new_positions.add((x, y + 1))
            if (x > 0) and (grid[y][x - 1] == '.'):
                new_positions.add((x - 1, y))
            if (x < width - 1) and (grid[y][x + 1] == '.'):
                new_positions.add((x + 1, y))
        positions = new_positions
    return len(positions)


def part1(task_input):
    grid = [list(row) for row in task_input.split('\n')]
    position = (0, 0)
    height = len(grid)
    width = len(grid[0])

    for j in range(height):
        for i in range(width):
            if grid[j][i] == 'S':
                grid[j][i] = '.'
                position = (i, j)
                break

    return get_field_count(grid, position, 64)


def part2(task_input):
    pass
