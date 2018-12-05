from itertools import cycle


resulting_frequency = sum


def calibration_frequency(frequencies):
    seen = set()
    running_sum = 0
    for frequency in frequencies:
        running_sum += frequency
        if running_sum in seen:
            return running_sum
        seen.add(running_sum)


def part1(day1input):
    frequencies = [int(num) for num in day1input.splitlines()]
    return resulting_frequency(frequencies)


def part2(day1input):
    frequencies = [int(num) for num in day1input.splitlines()]
    return calibration_frequency(cycle(frequencies))
