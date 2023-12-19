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


def part2(task_input):
    pass
