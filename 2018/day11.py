from functools import lru_cache


def hundreds_digit_or_zero(power_level):
    return int(power_level / 100) % 10


@lru_cache(maxsize=pow(2, 17))
def cell_power_level(x, y, grid_serial_number):
    # rack_id = x + 10
    # power_level = rack_id * y
    # power_level = power_level + grid_serial_number
    # power_level = power_level * rack_id
    # power_level = hundreds_digit_or_zero(power_level)
    # return power_level - 5
    return hundreds_digit_or_zero((((x + 10) * y) + grid_serial_number) * (x + 10)) - 5


class PowerGrid:
    """
    Power Grid implemented as an Integral Image (or a Summed Area Table)

    The summed area is cached (or memoized) with an LRU cache from functools
    (thanks Python standard library for not making me reinvent the wheel)

    """

    def __init__(self, serial_number, grid_size=300) -> None:
        super().__init__()
        self.serial_number = serial_number
        self.grid_size = grid_size + 1

    @lru_cache(maxsize=pow(2, 17))
    def summed_area(self, x, y):
        """
        Summed area above and to the left of x, y
        """
        if x < 0 or y < 0:
            return 0
        else:
            return (self.summed_area(x - 1, y)
                    + self.summed_area(x, y - 1)
                    - self.summed_area(x - 1, y - 1)
                    + cell_power_level(x, y, self.serial_number))

    def power_level(self, x, y, cell_pack_size):
        a = self.summed_area(x - 1, y - 1)
        b = self.summed_area(x - 1, y + cell_pack_size - 1)
        c = self.summed_area(x + cell_pack_size - 1, y - 1)
        d = self.summed_area(x + cell_pack_size - 1, y + cell_pack_size - 1)
        return d - b - c + a

    def best_cell_pack_location(self, cell_pack_size):
        cell_pack_power_levels = {(x, y): self.power_level(x, y, cell_pack_size)
                                  for y in range(1, self.grid_size - cell_pack_size)
                                  for x in range(1, self.grid_size - cell_pack_size)}
        return max(cell_pack_power_levels, key=cell_pack_power_levels.get)

    def best_cell_pack(self):
        best_cell_pack_location = (1, 1)
        best_cell_pack_size = 3
        best_cell_pack_power_level = self.power_level(1, 1, 3)
        for cell_pack_size in range(2, self.grid_size):
            for y in range(self.grid_size - cell_pack_size):
                for x in range(self.grid_size - cell_pack_size):
                    cell_pack_power_level = self.power_level(x, y, cell_pack_size)
                    if cell_pack_power_level > best_cell_pack_power_level:
                        best_cell_pack_location = (x, y)
                        best_cell_pack_size = cell_pack_size
                        best_cell_pack_power_level = cell_pack_power_level
        return best_cell_pack_location, best_cell_pack_size


def part1(grid_serial):
    power_grid = PowerGrid(int(grid_serial))
    return power_grid.best_cell_pack_location(3)


def part2(grid_serial):
    power_grid = PowerGrid(int(grid_serial))
    return power_grid.best_cell_pack()


def tests():

    assert cell_power_level(3, 5, 8) == 4
    assert cell_power_level(122, 79, 57) == -5
    assert cell_power_level(217, 196, 39) == 0
    assert cell_power_level(101, 153, 71) == 4

    assert part1('18') == (33, 45)
    assert part1('42') == (21, 61)

    assert part2('18') == ((90, 269), 16)
    assert part2('42') == ((232, 251), 12)

    print('Tests successful')


if __name__ == '__main__':
    tests()
