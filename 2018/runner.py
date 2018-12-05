import advent_of_code
import day1, day2, day3, day4


days = [
    day1,
    day2,
    day3,
    day4
]


def print_solutions_for_day(day, solver):
    print('Day {}:'.format(day))
    dayinput = advent_of_code.get_day_input(day)
    print(solver.part1(dayinput))
    print(solver.part2(dayinput))
    print()


def main():
    for day, solver in enumerate(days, start=1):
        print_solutions_for_day(day, solver)


if __name__ == '__main__':
    main()
