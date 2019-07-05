from collections import defaultdict

def pots_with_plants(pots):
    return [number for number, pot in enumerate(pots) if pot == '#']

def next_generation(planted_pots, notes):
    # I think I only have to check every pot that is within the note radius of a filled pot.
    # This should be the pots neighbors.
    # I need to just check all of the neighbors of this pot.
    note_radius = 2
    visited = defaultdict(bool)
    new_generation = []

    def is_planted(pot):
        representation = ''.join('#' if pot_ in planted_pots else '.' for pot_ in range(pot - 2, pot + 3))
        try:
            return notes[representation] == '#'
        except KeyError:
            return False

    for planted_pot in planted_pots:
        for pot in range(planted_pot - note_radius, planted_pot + note_radius + 1):
            if not visited[pot]:
                visited[pot] = True
                if is_planted(pot):
                    new_generation.append(pot)
    return new_generation

def old_next_generation(planted_pots, notes):
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

    import time

    initial_state = '#..#.#..##......###...###'
    generations = [pots_with_plants(initial_state)]
    gen = next_generation(generations[0], notes)
    last_difference = None
    last_sum = sum(gen)
    a_start_time = time.time()
    for i in range(50000):
        gen = next_generation(generations[i], notes)
        generation_sum = sum(gen)
        generations.append(gen)
        difference =generation_sum - last_sum
        if difference == last_difference:
            print("found diff: {}".format(difference))

        last_difference = difference
        last_sum = generation_sum
    a_end_time = time.time()

    # reset
    generations = [pots_with_plants(initial_state)]

    b_start_time = time.time()
    for i in range(50000):
        generations.append(old_next_generation(generations[i], notes))
    b_end_time = time.time()

    print(a_end_time - a_start_time) # 7.2298 seconds at 50000 generations
    print(b_end_time - b_start_time) # 8.2948 seconds at 50000 generations

    # # this is our answer here
    # print(sum(generations[20]))
    #
    # print_generations(generations)
    # print(pots_with_plants('.#....##....#####...#######....#.#..##.'))


    # At what generation N does sum(generation(N)) - sum(generation(N-1)) == sum(generation(N-1)) - sum(generation(N-2))?

    # how many times do we need to find the same difference in a row to consider it stabilized?

    # Take this difference at N, and extrapolate out to N = 50billion


if __name__ == '__main__':
    tests()
