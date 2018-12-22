""" --- Day 10: The Stars Align --- """

import re


point_regex = re.compile('position=<(?P<position>.+)> velocity=<(?P<velocity>.+)>')


def get_yrange_at_time(points, t):
    y_values = [point[1] + t * velocity[1] for point, velocity in points.items()]
    return max(y_values) - min(y_values)


def get_smallest_y_range_in_time_range(range_, points):
    times = {t: get_yrange_at_time(points, t) for t in range_}
    return min(times, key=times.get)


def point_view(points_in_time):
    max_x, max_y = max(points_in_time, key=lambda p: p[0])[0], max(points_in_time, key=lambda p: p[1])[1]
    min_x, min_y = min(points_in_time, key=lambda p: p[0])[0], min(points_in_time, key=lambda p: p[1])[1]
    board = []
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in points_in_time:
                board.append('#')
            else:
                board.append('.')
        board.append('\n')
    return ''.join(board)


def get_optimal_time(points):
    t = 0
    previous = get_yrange_at_time(points, 0)
    current = get_yrange_at_time(points, t + 1)
    while previous > current:
        t += 1
        previous = current
        current = get_yrange_at_time(points, t + 1)
    return t


def get_points(point_data):
    return {tuple(int(c) for c in d['position'].strip().split(', ')):
            tuple(int(c) for c in d['velocity'].strip().split(', '))
            for d in point_regex.finditer(point_data)}


def part1(point_data):
    points = get_points(point_data)
    t = get_optimal_time(points)
    points_in_time = [tuple(c + t * v for c, v in zip(point, velocity)) for point, velocity in points.items()]
    return point_view(points_in_time)


def part2(point_data):
    return get_optimal_time(get_points(point_data))


def tests():
    test_points = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

    test_word = """\
............
.#...#..###.
.#...#...#..
.#...#...#..
.#####...#..
.#...#...#..
.#...#...#..
.#...#...#..
.#...#..###.
............
"""

    assert part1(test_points) == test_word
    assert part2(test_points) == 3


if __name__ == '__main__':
    tests()
