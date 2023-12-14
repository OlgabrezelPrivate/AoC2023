def tilt_north(field):
    height = len(field)
    width = len(field[0])
    changed = True
    while changed:
        changed = False
        for j in range(height - 1):
            for i in range(width):
                if (field[j][i] == '.') and (field[j+1][i] == 'O'):
                    changed = True
                    field[j][i] = 'O'
                    field[j+1][i] = '.'


def tilt_west(field):
    height = len(field)
    width = len(field[0])
    changed = True
    while changed:
        changed = False
        for j in range(height):
            for i in range(width - 1):
                if (field[j][i] == '.') and (field[j][i+1] == 'O'):
                    changed = True
                    field[j][i] = 'O'
                    field[j][i+1] = '.'


def tilt_south(field):
    height = len(field)
    width = len(field[0])
    changed = True
    while changed:
        changed = False
        for j in range(1, height):
            for i in range(width):
                if (field[j][i] == '.') and (field[j-1][i] == 'O'):
                    changed = True
                    field[j][i] = 'O'
                    field[j-1][i] = '.'


def tilt_east(field):
    height = len(field)
    width = len(field[0])
    changed = True
    while changed:
        changed = False
        for j in range(height):
            for i in range(1, width):
                if (field[j][i] == '.') and (field[j][i-1] == 'O'):
                    changed = True
                    field[j][i] = 'O'
                    field[j][i-1] = '.'


def spin_cycle(field):
    tilt_north(field)
    tilt_west(field)
    tilt_south(field)
    tilt_east(field)


def load_on_north_axis(field):
    height = len(field)
    width = len(field[0])
    return sum(height - j for j in range(height) for i in range(width) if field[j][i] == 'O')


def part1(task_input):
    field = [list(row) for row in task_input.split('\n')]
    tilt_north(field)
    return load_on_north_axis(field)


FIELDS = dict()


def part2(task_input):
    field = [list(row) for row in task_input.split('\n')]
    total_spins = 1_000_000_000  # Total number of spins we are supposed to do
    final_spins = -1             # Final number of spins we actually do, since they result in the same field
    for spins in range(total_spins + 1):
        if final_spins == -1:
            field_tpl = tuple(tuple(t) for t in field)
            if field_tpl not in FIELDS:
                FIELDS[field_tpl] = spins
            else:
                cycle_length = spins - FIELDS[field_tpl]
                # After cycle_length spins, we end up with the same field
                # Calculate final number of spins needed:
                final_spins = total_spins % cycle_length
                while final_spins <= spins:
                    final_spins += cycle_length
        elif spins == final_spins:
            return load_on_north_axis(field)

        spin_cycle(field)
