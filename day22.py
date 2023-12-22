class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.cubes = {(x, y, z)
                      for x in range(min(x1, x2), max(x1, x2) + 1)
                      for y in range(min(y1, y2), max(y1, y2) + 1)
                      for z in range(min(z1, z2), max(z1, z2) + 1)}


def get_bricks(task_input):
    bricks = []
    for row in task_input.split('\n'):
        end1, end2 = row.split('~')
        x1, y1, z1 = map(int, end1.split(','))
        x2, y2, z2 = map(int, end2.split(','))
        bricks.append(Brick(x1, y1, z1, x2, y2, z2))
    return bricks


def fall_bricks(bricks):
    bricks_to_fall = bricks.copy()
    cubes_fallen = set()

    while len(bricks_to_fall):
        for i in range(len(bricks_to_fall) - 1, -1, -1):
            brick = bricks_to_fall[i]
            if any((cube[0], cube[1], cube[2] - 1) in cubes_fallen for cube in brick.cubes):
                bricks_to_fall.pop(i)
                cubes_fallen = cubes_fallen.union(brick.cubes)
                continue

            if any(cube[2] == 1 for cube in brick.cubes):
                bricks_to_fall.pop(i)
                cubes_fallen = cubes_fallen.union(brick.cubes)
                continue

            if any((cube[0], cube[1], cube[2] - 1) in other_brick.cubes
                   for cube in brick.cubes for other_brick in bricks_to_fall if other_brick != brick):
                continue

            brick.cubes = {(cube[0], cube[1], cube[2] - 1) for cube in brick.cubes}


def get_bricks_that_are_needed_to_support_other_bricks(bricks):
    bricks_that_are_needed_to_support_other_bricks = []

    for brick in bricks:
        if (0, 1, 4) in brick.cubes:
            pass
        all_bricks_above_have_other_supporter = True
        for brick_above in bricks:
            if brick_above == brick:
                continue

            if any((cube[0], cube[1], cube[2] - 1) in brick.cubes for cube in brick_above.cubes):
                for other_supporter in bricks:
                    if other_supporter == brick or other_supporter == brick_above:
                        continue

                    if any((cube[0], cube[1], cube[2] + 1) in brick_above.cubes for cube in other_supporter.cubes):
                        break
                else:
                    all_bricks_above_have_other_supporter = False
                    break

        if all_bricks_above_have_other_supporter:
            bricks_that_are_needed_to_support_other_bricks.append(brick)

    return bricks_that_are_needed_to_support_other_bricks


def part1(task_input):
    bricks = get_bricks(task_input)
    fall_bricks(bricks)
    return len(get_bricks_that_are_needed_to_support_other_bricks(bricks))


def part2(task_input):
    pass
