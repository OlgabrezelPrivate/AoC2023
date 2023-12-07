from functools import total_ordering


KINDS = ['HIGH', 'PAIR', 'TWOPAIRS', 'THREE', 'FULL', 'FOUR', 'FIVE']
CARDS = [['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],  # Part 1
         ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']]  # Part 2


@total_ordering
class Deck:
    def __init__(self, cards, task_part):
        self.cards = cards
        self.task_part = task_part
        self.kind_idx = KINDS.index(self.get_kind())

    def __eq__(self, other):
        return type(other) is Deck and all(self.cards[i] == other.cards[i] for i in range(5))

    def get_kind(self):
        if self.task_part == 2:
            # Gets the best card to replace jokers with. This is in any case just the card (other than a joker)
            # that already appears the most often in the deck. Since we are only determining the kind of deck here,
            # it doesn't matter which card the joker is replaced by in case of ties.
            card_counts = {c: self.cards.count(c) for c in self.cards if c != 'J'} or {'A': 5}
            best_card = next((x for x in card_counts if card_counts[x] == max(card_counts.values())))
            cards = self.cards.replace('J', best_card)
        else:
            cards = self.cards

        counts = sorted([cards.count(c) for c in CARDS[self.task_part - 1]], reverse=True)
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
            own_card = CARDS[self.task_part - 1].index(self.cards[i])
            other_card = CARDS[other.task_part - 1].index(other.cards[i])
            if own_card < other_card:
                return True
            if other_card < own_card:
                return False

        return False


def parse_input(task_input, task_part):
    decks = []
    for row in task_input.split('\n'):
        cards, bid = row.split(' ')
        decks.append((Deck(cards, task_part), int(bid)))
    return decks


def get_winnings(decks):
    sorted_decks = sorted(decks, key=lambda tpl: tpl[0])
    winnings = 0

    for i in range(len(sorted_decks)):
        winnings += sorted_decks[i][1] * (i + 1)

    return winnings


def part1(task_input):
    decks = parse_input(task_input, 1)
    return get_winnings(decks)


def part2(task_input):
    decks = parse_input(task_input, 2)
    return get_winnings(decks)
