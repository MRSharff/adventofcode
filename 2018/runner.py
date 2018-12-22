import advent_of_code
import importlib
import glob


days = {day[:-3]: importlib.import_module(day[:-3]) for day in glob.glob('day*.py')}


def print_solutions_for_day(day):
    print('Day {}:'.format(day))
    dayinput = advent_of_code.get_day_input(day)
    solver = days['day{}'.format(day)]
    for part in range(1, 3):
        part_solver = 'part{}'.format(part)
        if hasattr(solver, part_solver):
            print(getattr(solver, part_solver)(dayinput))
        else:
            print('No Solution for Day {} Part {}'.format(day, part))
    print()


def main():
    for day in range(1, len(days) + 1):
        print_solutions_for_day(day)


if __name__ == '__main__':
    main()
