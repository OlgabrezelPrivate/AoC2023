from functools import total_ordering


CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
KINDS = ['HIGH', 'PAIR', 'TWOPAIRS', 'THREE', 'FULL', 'FOUR', 'FIVE']


@total_ordering
class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.kind_idx = KINDS.index(self.get_kind())

    def __eq__(self, other):
        return type(other) is Deck and all(self.cards[i] == other.cards[i] for i in range(5))

    def get_kind(self):
        counts = sorted([self.cards.count(c) for c in CARDS], reverse=True)
        if counts[0] == 5:
            return 'FIVE'
        if counts[0] == 4:
            return 'FOUR'
        if counts[0] == 3:
            if counts[1] == 2:
                return 'FULL'
            return 'THREE'
        if counts[0] == 2:
            if counts[1] == 2:
                return 'TWOPAIRS'
            return 'PAIR'
        return 'HIGH'

    def __lt__(self, other):
        if self.kind_idx < other.kind_idx:
            return True
        if self.kind_idx > other.kind_idx:
            return False
        for i in range(5):
            own_card = CARDS.index(self.cards[i])
            other_card = CARDS.index(other.cards[i])
            if own_card < other_card:
                return True
            if other_card < own_card:
                return False

        return False


def parse_input(task_input):
    decks = []
    for row in task_input.split('\n'):
        cards, bid = row.split(' ')
        decks.append((Deck(list(cards)), int(bid)))
    return decks


def part1(task_input):
    decks = parse_input(task_input)
    sorted_decks = sorted(decks, key=lambda tpl: tpl[0])
    winnings = 0

    for i in range(len(sorted_decks)):
        winnings += sorted_decks[i][1] * (i + 1)

    return winnings


def part2(task_input):
    pass
