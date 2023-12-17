from dataclasses import dataclass, field
from math import inf
from heapq import heappop, heapify, heappush  # I freaking LOVE that you can just import anything


class Node:
    def __init__(self, x, y, dim, value):
        self.x = x
        self.y = y
        self.dimension = dim  # 0 - not moved. 1/2/3: moved right. 4/5/6: moved down. 7/8/9: moved left. 10/11/12: moved up.
        self.neighbors = []
        self.dist = inf if (x != 0) or (y != 0) or (dim != 0) else 0
        self.prev = None
        self.value = value


@dataclass(order=True)
class QueueEntry:
    priority: int
    item: Node = field(compare=False)


def build_graph_part1(grid):
    height = len(grid)
    width = len(grid[0])
    nodes = [[[Node(x, y, dim, grid[y][x]) for x in range(width)] for y in range(height)] for dim in range(13)]
    nodes_flat = [n for dim in range(13) for row in nodes[dim] for n in row]

    for n in nodes_flat:
        if n.x > 0 and n.dimension not in [9, 1, 2, 3]:
            new_dim = 7 if n.dimension <= 6 or n.dimension >= 10 else n.dimension + 1
            n.neighbors.append(nodes[new_dim][n.y][n.x - 1])
        if n.x < width - 1 and n.dimension not in [3, 7, 8, 9]:
            new_dim = 1 if n.dimension <= 0 or n.dimension >= 4 else n.dimension + 1
            n.neighbors.append(nodes[new_dim][n.y][n.x + 1])
        if n.y > 0 and n.dimension not in [12, 4, 5, 6]:
            new_dim = 10 if n.dimension <= 9 else n.dimension + 1
            n.neighbors.append(nodes[new_dim][n.y - 1][n.x])
        if n.y < height - 1 and n.dimension not in [6, 10, 11, 12]:
            new_dim = 4 if n.dimension <= 3 or n.dimension >= 7 else n.dimension + 1
            n.neighbors.append(nodes[new_dim][n.y + 1][n.x])

    return nodes, nodes_flat


def dijkstra(nodes, nodes_flat):
    height = len(nodes[0])
    width = len(nodes[0][0])

    Q = [QueueEntry(n.dist, n) for n in nodes_flat]
    heapify(Q)

    found_destination_in_dimensions = set()
    deleted = set()

    while Q:
        u = heappop(Q)
        if (u.priority, u.item.x, u.item.y, u.item.dimension) in deleted:
            deleted.remove((u.priority, u.item.x, u.item.y, u.item.dimension))
            continue

        if u.item.x == width - 1 and u.item.y == height - 1:
            found_destination_in_dimensions.add(u.item.dimension)
            if len(found_destination_in_dimensions) == 13:
                break

        for v in u.item.neighbors:
            alternative = u.item.dist + v.value
            if alternative < v.dist:
                deleted.add((v.dist, v.x, v.y, v.dimension))
                v.dist = alternative
                v.prev = u.item
                heappush(Q, QueueEntry(v.dist, v))

    # For debugging purposes, here is how to output the optimal path
    """
    dest = sorted([nodes[dim][-1][-1] for dim in range(13)], key=lambda n: n.dist)[0]
    path = [(dest.x, dest.y)]
    while dest.prev:
        dest = dest.prev
        path.insert(0, (dest.x, dest.y))
    print(path)
    """

    return min([nodes[dim][-1][-1].dist for dim in range(13)])


def part1(task_input):
    grid = [[int(x) for x in row] for row in task_input.split('\n')]
    nodes, nodes_flat = build_graph_part1(grid)
    return dijkstra(nodes, nodes_flat)


def part2(task_input):
    pass
