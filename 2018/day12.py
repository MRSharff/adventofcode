

def pots_with_plants(pots):
    return [number for number, pot in enumerate(pots) if pot == '#']

def next_generation(planted_pots, notes):
    # pot numbers that are within the note radius of the min or the max
    # LLCRR not has a radius of 2
    # if the left most pot is pot number 1, then it is possible for pot number 1 to affect a pot 2 to the left
    def remains_planted(pot):
        representation = ''.join('#' if pot_ in planted_pots else '.' for pot_ in range(pot - 2, pot + 3))
        try:
            return notes[representation] == '#'
        except KeyError:
            return False

    return [pot for pot in range(min(planted_pots) - 2, max(planted_pots) + 3) if remains_planted(pot)]

def generation(gen, initial_state, notes):
    pots = pots_with_plants(initial_state)
    for _ in range(gen):
        pots = next_generation(pots, notes)
    return pots


def print_generations(generations):

    leftmost = min(generation[0] for generation in generations)

    for i, generation in enumerate(generations):
        potstring = ''.join('#' if pot in generation else "." for pot in range(generation[0], generation[-1] + 1))
        zfill_pots = -(leftmost - generation[0] - 1) * '.'
        print(f'{i}: {zfill_pots}{potstring}')



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
