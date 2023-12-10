class Graph:
    def __init__(self, width, height, adj_lists, start):
        self.width = width
        self.height = height
        self.adj_lists = adj_lists
        self.start = start

    def find_main_loop(self):
        loop = [self.start]
        pos = self.adj_lists[self.start[0]][self.start[1]][0]
        while pos != self.start:
            loop.append(pos)
            pos1 = self.adj_lists[pos[0]][pos[1]][0]
            pos2 = self.adj_lists[pos[0]][pos[1]][1]
            pos = pos2 if loop[-2] == pos1 else pos1
        loop.append(self.start)
        return loop


def parse_input(task_input):
    lines = task_input.split('\n')
    height = len(lines)
    width = len(lines[0])
    start = tuple()
    adj_lists = [[[] for i in range(width)] for j in range(height)]
    for j in range(height):
        for i in range(width):
            match lines[j][i]:
                case '|':
                    adj_lists[j][i].append((j-1, i))
                    adj_lists[j][i].append((j+1, i))
                case '-':
                    adj_lists[j][i].append((j, i-1))
                    adj_lists[j][i].append((j, i+1))
                case 'L':
                    adj_lists[j][i].append((j-1, i))
                    adj_lists[j][i].append((j, i+1))
                case 'J':
                    adj_lists[j][i].append((j-1, i))
                    adj_lists[j][i].append((j, i-1))
                case '7':
                    adj_lists[j][i].append((j, i-1))
                    adj_lists[j][i].append((j+1, i))
                case 'F':
                    adj_lists[j][i].append((j, i+1))
                    adj_lists[j][i].append((j+1, i))
                case 'S':
                    start = (j, i)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if start in adj_lists[start[0] + j][start[1] + i]:
                adj_lists[start[0]][start[1]].append((start[0] + j, start[1] + i))

    return Graph(width, height, adj_lists, start)


def part1(task_input):
    graph = parse_input(task_input)
    loop = graph.find_main_loop()
    return len(loop) // 2


def part2(task_input):
    pass
