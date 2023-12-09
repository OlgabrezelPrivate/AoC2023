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


def traverse_graph(start_node, instructions, nodes):
    cur_node = start_node
    steps = 0
    while cur_node != 'ZZZ':
        cur_node = nodes[cur_node][0] if instructions[steps % len(instructions)] == 'L' else nodes[cur_node][1]
        steps += 1
    return steps


def part1(task_input):
    instructions, nodes = parse_input(task_input)
    return traverse_graph('AAA', instructions, nodes)


def part2(task_input):
    pass
