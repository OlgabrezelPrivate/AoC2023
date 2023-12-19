class Workflow:
    def __init__(self, s):
        name, rest = s.split('{')
        self.name = name

        instructions = rest[:-1].split(',')
        self.instructions = []
        for ins in instructions[:-1]:
            component = ins[0]
            comparison = ins[1]
            rest, result = ins.split(':')
            value = int(rest[2:])
            self.instructions.append((component, comparison, value, result))

        self.else_branch = instructions[-1]

    def apply(self, part):
        for ins in self.instructions:
            match ins[1]:
                case '<':
                    if part[ins[0]] < ins[2]:
                        return ins[3]
                case '>':
                    if part[ins[0]] > ins[2]:
                        return ins[3]
        return self.else_branch


def parse_part(s):
    components = [x.split('=') for x in s[1:-1].split(',')]
    return {c[0]: int(c[1]) for c in components}


def is_accepted_part(named_workflows, part):
    workflow_name = 'in'
    while True:
        match named_workflows[workflow_name].apply(part):
            case 'R':
                return False
            case 'A':
                return True
            case val:
                workflow_name = val


def part1(task_input):
    instructions = task_input.split('\n\n')
    workflows = [Workflow(x) for x in instructions[0].split('\n')]
    named_workflows = {x.name: x for x in workflows}
    parts = [parse_part(x) for x in instructions[1].split('\n')]

    result = 0

    for p in parts:
        if is_accepted_part(named_workflows, p):
            result += p['x'] + p['m'] + p['a'] + p['s']
    return result


def accepted_parts_count(named_workflows, workflow_name, ranges):
    result = 0
    if workflow_name == 'R':
        return 0
    if workflow_name == 'A':
        return ((ranges['x'][1] - ranges['x'][0] + 1) * (ranges['m'][1] - ranges['m'][0] + 1) *
                (ranges['a'][1] - ranges['a'][0] + 1) * (ranges['s'][1] - ranges['s'][0] + 1))

    workflow = named_workflows[workflow_name]
    for ins in workflow.instructions:
        match ins[1]:
            case '<':
                if ranges[ins[0]][1] < ins[2]:  # the ENTIRE range satisfies the condition - can stop the iteration here
                    return result + accepted_parts_count(named_workflows, ins[3], ranges)
                if ranges[ins[0]][0] < ins[2]:  # Part of the range satisfies the condition - continue iterating with rest
                    smaller_ranges = ranges.copy()
                    smaller_ranges[ins[0]] = (smaller_ranges[ins[0]][0], ins[2] - 1)
                    result += accepted_parts_count(named_workflows, ins[3], smaller_ranges)
                    ranges[ins[0]] = (ins[2], ranges[ins[0]][1])
            case '>':
                if ranges[ins[0]][0] > ins[2]:  # the ENTIRE range satisfies the condition - can stop the iteration here
                    return result + accepted_parts_count(named_workflows, ins[3], ranges)
                if ranges[ins[0]][1] > ins[2]:  # Part of the range satisfies the condition - continue iterating with rest
                    larger_ranges = ranges.copy()
                    larger_ranges[ins[0]] = (ins[2] + 1, larger_ranges[ins[0]][1])
                    result += accepted_parts_count(named_workflows, ins[3], larger_ranges)
                    ranges[ins[0]] = (ranges[ins[0]][0], ins[2])

    return result + accepted_parts_count(named_workflows, workflow.else_branch, ranges)


def part2(task_input):
    workflows = [Workflow(x) for x in task_input.split('\n\n')[0].split('\n')]
    named_workflows = {x.name: x for x in workflows}

    x, m, a, s = (1, 4000), (1, 4000), (1, 4000), (1, 4000)
    return accepted_parts_count(named_workflows, 'in', {'x': x, 'm': m, 'a': a, 's': s})
