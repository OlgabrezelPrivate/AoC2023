class Graph:
    def __init__(self, width, height, adj_lists, start, tiles):
        self.width = width
        self.height = height
        self.adj_lists = adj_lists
        self.start = start
        self.tiles = tiles

    def find_main_loop(self):
        loop = [self.start]
        pos = self.adj_lists[self.start[0]][self.start[1]][0]
        while pos != self.start:
            loop.append(pos)
            pos1 = self.adj_lists[pos[0]][pos[1]][0]
            pos2 = self.adj_lists[pos[0]][pos[1]][1]
            pos = pos2 if loop[-2] == pos1 else pos1
        return set(loop)


def parse_input(task_input):
    lines = [list(x) for x in task_input.split('\n')]
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

    start_up, start_right, start_down, start_left = False, False, False, False
    for i in [-1, 1]:
        if start in adj_lists[start[0]][start[1] + i]:
            adj_lists[start[0]][start[1]].append((start[0], start[1] + i))
            if i == -1:
                start_left = True
            else:
                start_right = True

    for j in [-1, 1]:
        if start in adj_lists[start[0] + j][start[1]]:
            adj_lists[start[0]][start[1]].append((start[0] + j, start[1]))
            if j == -1:
                start_up = True
            else:
                start_down = True

    match (start_up, start_right, start_down, start_left):
        case (False, False, True, True):
            lines[start[0]][start[1]] = '7'
        case (False, True, False, True):
            lines[start[0]][start[1]] = '-'
        case (False, True, True, False):
            lines[start[0]][start[1]] = 'F'
        case (True, False, False, True):
            lines[start[0]][start[1]] = 'J'
        case (True, False, True, False):
            lines[start[0]][start[1]] = '|'
        case (True, True, False, False):
            lines[start[0]][start[1]] = 'L'

    return Graph(width, height, adj_lists, start, lines)


def part1(task_input):
    graph = parse_input(task_input)
    loop = graph.find_main_loop()
    return len(loop) // 2


def part2(task_input):
    graph = parse_input(task_input)
    loop = graph.find_main_loop()

    enclosed_count = 0
    for j in range(graph.height):
        i = 0
        inside = False
        while i < graph.width:
            if (j, i) in loop:
                match graph.tiles[j][i]:
                    case '|':
                        inside = not inside

                    case 'F':
                        i += 1
                        while graph.tiles[j][i] == '-':
                            i += 1
                        if graph.tiles[j][i] == 'J':
                            inside = not inside

                    case 'L':
                        i += 1
                        while graph.tiles[j][i] == '-':
                            i += 1
                        if graph.tiles[j][i] == '7':
                            inside = not inside
            elif inside:
                enclosed_count += 1

            i += 1

    return enclosed_count
