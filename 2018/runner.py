import advent_of_code
import day1, day2, day3, day4


days = [
    day1,
    day2,
    day3,
    day4
]


if __name__ == '__main__':
    for day, solution in enumerate(days, start=1):
        print('Day {}:'.format(day))
        dayinput = advent_of_code.get_day_input(day)
        print(solution.part1(dayinput))
        print(solution.part2(dayinput))
        print()
