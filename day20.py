from abc import ABC, abstractmethod
import math
from typing import Optional, List


class Module(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    # Returns None if no pulse is sent, False for a low and True for a high pulse
    def on_pulse(self, from_module_name: str, is_high: bool) -> Optional[bool]:
        pass

    def connect_to(self, connected_to: List[str]):
        self.connected_to = connected_to


class Flipflop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.on = False

    def on_pulse(self, from_module_name: str, is_high: bool) -> Optional[bool]:
        if not is_high:
            self.on = not self.on
            return self.on


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.remember = dict()

    def add_input(self, input_name):
        self.remember[input_name] = False

    def on_pulse(self, from_module_name: str, is_high: bool) -> Optional[bool]:
        self.remember[from_module_name] = is_high
        return not all(self.remember[x] for x in self.remember)


class Broadcaster(Module):
    def __init(self, name):
        super().__init__(name)

    def on_pulse(self, from_module_name: str, is_high: bool) -> Optional[bool]:
        return is_high


def get_modules(task_input):
    modules = dict()
    rows = task_input.split('\n')

    # First pass - create all the modules
    for row in rows:
        name = row.split(' -> ')[0]
        if name == 'broadcaster':
            modules[name] = Broadcaster(name)
        elif name.startswith('%'):
            modules[name[1:]] = Flipflop(name[1:])
        else:  # name.startswith('&')
            modules[name[1:]] = Conjunction(name[1:])

    # Second pass - connect all modules to their outputs / add inputs to conjunctions
    for row in rows:
        name, rest = row.split(' -> ')
        connected_to = rest.split(', ')
        if name != 'broadcaster':
            name = name[1:]

        modules[name].connect_to(connected_to)
        for connected in modules[name].connected_to:
            if (connected in modules) and (type(modules[connected]) is Conjunction):
                modules[connected].add_input(name)

    return modules


def part1(task_input):
    modules = get_modules(task_input)
    low_pulses = 0
    high_pulses = 0

    for i in range(1000):
        pulses = [('button', 'broadcaster', False)]
        low_pulses += 1

        while len(pulses):
            from_module_name, to_module_name, is_high = pulses.pop(0)
            if to_module_name in modules:
                to_module = modules[to_module_name]
                result = to_module.on_pulse(from_module_name, is_high)
                if result is not None:
                    pulses += [(to_module_name, x, result) for x in to_module.connected_to]
                    if result:
                        high_pulses += len(to_module.connected_to)
                    else:
                        low_pulses += len(to_module.connected_to)

    return low_pulses * high_pulses


def part2(task_input):
    modules = get_modules(task_input)
    presses = 0
    magic_module = next(x for x in modules if 'rx' in modules[x].connected_to)  # the one module that sends a low to rx.
    highs = {x: None for x in modules if magic_module in modules[x].connected_to}

    while True:
        presses += 1
        pulses = [('button', 'broadcaster', False)]

        while len(pulses):
            from_module_name, to_module_name, is_high = pulses.pop(0)

            # This is so lame. Magically, all of those send a high pulse periodically to the magic module.
            # Even more magically, all periods start at 0. So just find the first time each of them sends
            # a high pulse, and take the lcm of all these times. This feels like a recycled riddle from day 8, sadly.
            # And I already didn't like day 8.
            if (to_module_name == magic_module) and is_high and (highs[from_module_name] is None):
                highs[from_module_name] = presses
                if all(highs[x] is not None for x in highs):
                    return math.lcm(*highs.values())

            if to_module_name in modules:
                to_module = modules[to_module_name]
                result = to_module.on_pulse(from_module_name, is_high)
                if result is not None:
                    pulses += [(to_module_name, x, result) for x in to_module.connected_to]
