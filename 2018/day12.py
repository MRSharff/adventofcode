

def pots_with_plants(pots):
    return [number for number, pot in enumerate(pots) if pot == '#']

def next_generation(planted_pots, notes):
    def remains_planted(pot):
        representation = ''.join('#' if pot_ in planted_pots else '.' for pot_ in range(pot - 2, pot + 3))
        try:
            return notes[representation] == '#'
        except KeyError:
            return False

    return [pot for pot in range(min(planted_pots), max(planted_pots) + 1) if remains_planted(pot)]

def generation(gen, initial_state, notes):
    pots = pots_with_plants(initial_state)
    for _ in range(gen):
        pots = next_generation(pots, notes)
    return pots


def remains_planted(pot, notes):
    representation = ''.join('#' if pot_ in planted_pots else '.' for pot_ in range(pot - 2, pot + 3))
    try:
        return notes[representation] == '#'
    except KeyError:
        return False

class Generation:

    def __init__(self, planted_pots, notes) -> None:
        super().__init__()
        self.planted_pots = planted_pots
        self.width = self.planted_pots[0] + self.planted_pots[-1]
        self.notes = notes

    def remains_planted(self, pot):
        representation = ''.join('#' if pot_ in self.planted_pots else '.' for pot_ in range(pot - 2, pot + 3))
        try:
            return self.notes[representation] == '#'
        except KeyError:
            return False

    def __next__(self):
        return [pot for pot in range(self.planted_pots[0], self.planted_pots[-1] + 1) if self.remains_planted(pot)]

    def __str__(self) -> str:
        return super().__str__()


def print_generations(generations):

    leftmost = min(generation[0] for generation in generations)

    for i, generation in enumerate(generations):
        potstring = ''.join('#' if pot in generation else "." for pot in range(generation[0], generation[-1] + 1))
        print(f'{i}: {potstring.rjust(leftmost + generation[0], ".")}')



def tests():

    # planted_pots returns a list of pot numbers that are planted
    assert pots_with_plants('#..##....') == [0, 3, 4]
    assert pots_with_plants('....#')


    notes = {''.join(note[:5]): note[-1] for note in """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
    """.splitlines()}

    assert notes['..#..'] == '#'

    print(next_generation(pots_with_plants('#..#.#..##......###...###'), notes))
    print(pots_with_plants('#...#....#.....#..#..#..#'))

    pots = []

    assert next_generation(pots_with_plants('#..#.#..##......###...###'), notes) == pots_with_plants('#...#....#.....#..#..#..#')

    initial_state = '#..#.#..##......###...###'
    generations = [pots_with_plants(initial_state)]
    for i in range(20):
        generations.append(next_generation(generations[i], notes))

    print_generations(generations)
    print(pots_with_plants('.#....##....#####...#######....#.#..##.'))

    # print(generation(20, initial_state, notes))
    # print(pots_with_plants('.#....##....#####...#######....#.#..##.'))
    # assert generation(20, initial_state, notes) == pots_with_plants('.#....##....#####...#######....#.#..##.')




if __name__ == '__main__':
    tests()
