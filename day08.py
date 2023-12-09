import math


def parse_input(task_input):
    # Return the nodes as a Dict[NodeId, Tuple[LeftNodeId, RightNodeId]]
    # The instructions as a string
    instructions, nodes_raw = task_input.split('\n\n')
    nodes = dict()
    for line in nodes_raw.split('\n'):
        nodeid, rest = line.split(' = ')
        left, right = rest[1:-1].split(', ')
        nodes[nodeid] = (left, right)

    return instructions, nodes


def traverse_graph(start_node, instructions, nodes, part):
    cur_node = start_node
    steps = 0
    while (part == 1 and cur_node != 'ZZZ') or (part == 2 and not cur_node.endswith('Z')):
        cur_node = nodes[cur_node][0] if instructions[steps % len(instructions)] == 'L' else nodes[cur_node][1]
        steps += 1
    return steps


def part1(task_input):
    instructions, nodes = parse_input(task_input)
    return traverse_graph('AAA', instructions, nodes, 1)


def part2(task_input):
    # This task was all about finding and exploiting patterns in the input data. It turns out that the searched number
    # is just the lowest common multiple of the numbers of steps it takes from each start node to get to a destination node.

    instructions, nodes = parse_input(task_input)
    start_nodes = [node for node in nodes if node.endswith('A')]
    steps = []

    for start_node in start_nodes:
        steps.append(traverse_graph(start_node, instructions, nodes, 2))
    return math.lcm(*steps)
