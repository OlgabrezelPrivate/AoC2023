from copy import deepcopy
import multiprocessing
from functools import partial


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
    bricks_that_moved = set()

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
            bricks_that_moved.add(brick)

    return len(bricks_that_moved)


def get_upper_bricks(bricks):
    upper_bricks = []

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
            upper_bricks.append(brick)

    return upper_bricks


def part1(task_input):
    print("Part 1 takes some 40 seconds to run, please wait...")
    bricks = get_bricks(task_input)
    fall_bricks(bricks)
    return len(get_upper_bricks(bricks))


def get_falling_count_when_evaporating(brick, bricks, upper_bricks):
    if brick not in upper_bricks:
        bricks_copy = [deepcopy(b) for b in bricks if b != brick]
        return fall_bricks(bricks_copy)
    return 0


def part2(task_input):
    print("If you thought, that was long... Part 2 takes about 22 minutes and uses all cpu cores.\nEnjoy, please wait...")
    bricks = get_bricks(task_input)
    fall_bricks(bricks)
    upper_bricks = set(get_upper_bricks(bricks))

    with multiprocessing.Pool() as pool:
        counts = pool.map(partial(get_falling_count_when_evaporating, bricks=bricks,
                                  upper_bricks=upper_bricks), bricks)

    return sum(counts)
