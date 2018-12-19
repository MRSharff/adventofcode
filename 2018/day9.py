""" --- Day 9: Marble Mania --- """

import re

from collections import deque, defaultdict


def marble_game(player_count, marble_count):
    score = defaultdict(int)
    circle = deque([0])
    # current marble is always at the head of the deque
    for marble in range(1, marble_count + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            score[marble % player_count] += circle.popleft() + marble
        else:
            circle.rotate(-2)
            circle.insert(0, marble)
    return max(score.values())


def tests():
    assert marble_game(9, 25) == 32

    assert marble_game(10, 1618) == 8317
    assert marble_game(13, 7999) == 146373
    assert marble_game(17, 1104) == 2764
    assert marble_game(21, 6111) == 54718
    assert marble_game(30, 5807) == 37305

    assert part1('10 players; last marble is worth 1618 points') == 8317
    assert part1('13 players; last marble is worth 7999 points') == 146373
    assert part1('17 players; last marble is worth 1104 points') == 2764
    assert part1('21 players; last marble is worth 6111 points') == 54718
    assert part1('30 players; last marble is worth 5807 points') == 37305


def part1(game_settings):
    players, marbles = map(int, re.findall(r'\d+', game_settings))
    return marble_game(players, marbles)


def part2(game_settings):
    players, marbles = map(int, re.findall(r'\d+', game_settings))
    return marble_game(players, marbles * 100)


if __name__ == '__main__':
    tests()
    print(part1('466 players; last marble is worth 71436 points'))
    import time
    start = time.time()
    print(part2('466 players; last marble is worth 71436 points'))
    print('time: {}'.format(time.time() - start))
