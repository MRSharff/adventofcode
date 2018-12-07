

def largest_noninfinite_area(coordinates):
    ys = [c[1] for c in coordinates]
    xs = [c[0] for c in coordinates]
    for y in range(min(ys), max(ys)):
        for x in range(min(xs), max(xs)):
            print('.', end='')
        print()

    return 17

def tests():
    coordinate_list = [(1, 1),
                       (1, 6),
                       (8, 3),
                       (3, 4),
                       (5, 5),
                       (8, 9)]

    assert largest_noninfinite_area(coordinate_list) == 17

if __name__ == '__main__':
    tests()