from itertools import cycle

# def strategize(notes):
#     pot_map = {''.join(note[:5]): note[-1] for note in notes}
#     def strategy(pots):
#         return pot_map.get(pots, '.')
#     return strategy


# def spread(pots, consideration):
#     """
#     :param pots:
#     :return: a new generation of plants in pots
#     """
#     new_pots = [*pots[:2]]
#     for i in range(2, len(pots) - 2):
#         pattern = consideration[:5]
#         pots_to_consider = pots[i - 2: i + 3]
#         new_pots.append(consideration[-1] if pots_to_consider == pattern else pots[i])
#     return ''.join([*new_pots, *pots[-2:]])

def spread(pots, strategy):
    new_pots = []
    for i in range(2, len(pots) - 2):
        span = ''.join(pots[i - 2: i + 3])
        new_pots.append(strategy.get(span, '.'))
    return [*new_pots, '.', '.']


# def spreadlr(left_pots, right_pots, strategy):
#     new_left_pots = []
#
#     for i in range(2, len(left_pots) - 2):
#
#
#
#
#     new_pots = pots[:2]
#     for i in range(2, len(pots) - 2):
#         new_pots.append(strategy(''.join(pots[i - 2: i + 3])))
#     return [*new_pots]



def tests():
    pot_input = '#..#.#..##......###...###'
    pots = [*iter('#..#.#..##......###...###'), *['.'] * 20]
    notes = """...## => #
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
####. => #"""

    left_pots = ['.'] * 20
    right_pots = pots

    right_spread_strategy = {''.join(note[:5]): note[-1] for note in notes.splitlines()}
    left_spread_strategy = {''.join(reversed(note[:5])): note[-1] for note in notes.splitlines()}

    generations = []
    for i in range(20):
        generations.append(''.join([*reversed(left_pots), *right_pots]))
        # print('{:2d}: {}'.format(i, ''.join([*reversed(left_pots), *right_pots])))
        new_left_pots = spread([*reversed(right_pots[:2]), *left_pots], left_spread_strategy)
        right_pots = spread([*reversed(left_pots[:2]), *right_pots], right_spread_strategy)
        left_pots = new_left_pots
    generations.append(''.join([*reversed(left_pots), *right_pots]))
    # print('{:2d}: {}'.format(20, ''.join([*reversed(left_pots), *right_pots])))
    total = 0
    for k, pot in enumerate(left_pots, start=1):
        if pot == '#':
            total -= k
    for k, pot in enumerate(right_pots):
        if pot == '#':
            total += k
    print(total)

    for i, generation in enumerate(generations):
        print('{:2d}: {}'.format(i, generation[17:56]))
    # for _, note in zip(range(20), cycle(n)):
    #     print(pots)
    #     pots = spread(pots, note)
    # print(pots)


def main():
    pot_input = '###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#'
    pots = [*iter(pot_input), *['.'] * 50]
    notes = """..### => #
..... => .
..#.. => .
.###. => .
...## => #
#.### => .
#.#.# => #
##..# => .
##.## => #
#...# => .
..##. => .
##.#. => .
...#. => .
#..#. => #
.#### => #
.#..# => #
##... => #
.##.# => .
....# => .
#.... => .
.#.#. => #
.##.. => .
###.# => #
####. => .
##### => #
#.##. => #
.#... => #
.#.## => #
###.. => #
#..## => .
#.#.. => #
..#.# => .""".splitlines()

    left_pots = ['.'] * 20
    right_pots = pots

    right_spread_strategy = {''.join(note[:5]): note[-1] for note in notes}
    left_spread_strategy = {''.join(reversed(note[:5])): note[-1] for note in notes}

    generations = []
    for i in range(20):
        generations.append(''.join([*reversed(left_pots), *right_pots]))
        # print('{:2d}: {}'.format(i, ''.join([*reversed(left_pots), *right_pots])))
        new_left_pots = spread([*reversed(right_pots[:2]), *left_pots], left_spread_strategy)
        right_pots = spread([*reversed(left_pots[:2]), *right_pots], right_spread_strategy)
        left_pots = new_left_pots
    generations.append(''.join([*reversed(left_pots), *right_pots]))
    # print('{:2d}: {}'.format(20, ''.join([*reversed(left_pots), *right_pots])))
    total = 0
    for k, pot in enumerate(left_pots, start=1):
        if pot == '#':
            total -= k
    for k, pot in enumerate(right_pots):
        if pot == '#':
            total += k
    print(total)

    # sums[20] = sum(-k if pot == '#' else 0 for k, pot in enumerate(['.', *left_pots], start=1))
    # sums[20] += sum(k if pot == '#' else 0 for k, pot in enumerate([right_pots], start=1))
    #
    #
    # print(sums[20])


if __name__ == '__main__':
    # tests()
    main()