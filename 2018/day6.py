from collections import defaultdict


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_closest(coordinate, coordinates):
    distances = defaultdict(list)
    for other_coordinate in coordinates:
        distances[manhattan_distance(coordinate, other_coordinate)].append(other_coordinate)
    closest = min(distances)
    if len(distances[closest]) > 1:
        return None
    return distances[closest][0]


def largest_noninfinite_area(coordinates):
    non_edge_coordinates = coordinates[:]
    areas = defaultdict(int)
    ys = sorted(c[1] for c in coordinates)
    xs = sorted(c[0] for c in coordinates)
    minx, maxx = (xs[0], xs[-1])
    miny, maxy = (ys[0], ys[-1])
    for y in range(miny, maxy + 1):
        is_y_edge = (y == miny or y == maxy)
        for x in range(minx, maxx + 1):
            is_x_edge = (x == minx or x == maxx)
            closest = get_closest((x, y), coordinates)
            if closest in non_edge_coordinates and (is_y_edge or is_x_edge):
                non_edge_coordinates.remove(closest)
            else:
                areas[closest] += 1
    return areas[max(non_edge_coordinates, key=areas.get)]


def get_region_size_of_coords_within_distance(distance, coordinates):
    ys = sorted(c[1] for c in coordinates)
    xs = sorted(c[0] for c in coordinates)
    minx, maxx = (xs[0], xs[-1])
    miny, maxy = (ys[0], ys[-1])
    return sum(1 for x in range(minx, maxx + 1)
               for y in range(miny, maxy + 1)
               if sum(manhattan_distance((x, y), c) for c in coordinates) < distance)


def part1(coordinates_input):
    clines = [cline.split(', ') for cline in coordinates_input.strip().splitlines()]
    coordinates = [(int(c[0]), int(c[1])) for c in clines]
    return largest_noninfinite_area(coordinates)


def part2(coordinates_input):
    clines = [cline.split(', ') for cline in coordinates_input.strip().splitlines()]
    coordinates = [(int(c[0]), int(c[1])) for c in clines]
    return get_region_size_of_coords_within_distance(10000, coordinates)


def tests():
    coordinate_list = [(1, 1),
                       (1, 6),
                       (8, 3),
                       (3, 4),
                       (5, 5),
                       (8, 9)]

    assert largest_noninfinite_area(coordinate_list) == 17
    assert get_region_size_of_coords_within_distance(32, coordinate_list) == 16


if __name__ == '__main__':
    tests()