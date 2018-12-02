from itertools import cycle

from advent_of_code import get_day_input


def resulting_frequency(frequency_changes):
    return sum(frequency_changes)


def calibration_frequency(frequencies):
    seen = set()
    running_sum = 0
    for frequency in frequencies:
        running_sum += frequency
        if running_sum in seen:
            return running_sum
        seen.add(running_sum)


def frequency_generator(frequencies):
    return cycle(frequencies)


if __name__ == '__main__':
    day_1_input = [int(num) for num in get_day_input(1).splitlines()]
    print(resulting_frequency(day_1_input))
    print(calibration_frequency(frequency_generator(day_1_input)))
