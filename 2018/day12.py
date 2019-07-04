

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

    assert next_generation(pots_with_plants('#..#.#..##......###...###'), notes) == pots_with_plants('#...#....#.....#..#..#..#')




if __name__ == '__main__':
    tests()
