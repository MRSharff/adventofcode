import datetime

from collections import defaultdict


def parse_date(log_line):
    date_string = log_line[log_line.index('[') + 1:log_line.index(']')]
    return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')


def get_guard_number(log_line):
    guard_fh = log_line[log_line.index('#') + 1:]
    return int(guard_fh[:guard_fh.index(' ')])


def make_shift(log_line):
    return {'date': parse_date(log_line), 'asleep': []}


def make_guard(guard_number):
    return {'ID': guard_number, 'shifts': []}


def get_guards_and_shifts(schedule_log):
    guards = {}
    shifts = []
    current_shift = None
    sleep_start = None
    for log_line in schedule_log:
        if "Guard" in log_line:
            if current_shift is not None:
                shifts.append(current_shift)
            guard_number = get_guard_number(log_line)
            if guard_number not in guards:
                guards[guard_number] = make_guard(guard_number)
            current_shift = make_shift(log_line)
            current_shift['guard'] = guards[guard_number]
            current_shift['guard']['shifts'].append(current_shift)
        if 'sleep' in log_line:
            sleep_start = parse_date(log_line).minute
        if 'wake' in log_line:
            current_shift['asleep'].append(range(sleep_start, parse_date(log_line).minute))
    shifts.append(current_shift)
    return guards, shifts


def get_total_sleep(guard):
    return sum(len(sleep) for shift in guard['shifts'] for sleep in shift['asleep'])


def get_sleepiest_guard(guards):
    return max(guards.values(), key=get_total_sleep)


def get_minutes_slept(guard):
    minutes_slept = defaultdict(int)
    for shift in guard['shifts']:
        for sleep in shift['asleep']:
            for minute in sleep:
                minutes_slept[minute] += 1
    return minutes_slept


def get_sleepiest_minute(guard):
    minutes_slept = get_minutes_slept(guard)
    minute = max(minutes_slept, key=minutes_slept.get)
    return minute, minutes_slept[minute]


def get_guard_most_frequently_asleep_on_same_minute(guards):
    sleepiest_minute_counts = {ID: get_sleepiest_minute(guard)[1] for ID, guard in guards.items() if
                               any(len(shift['asleep']) > 0 for shift in guard['shifts'])}
    return guards[max(sleepiest_minute_counts, key=sleepiest_minute_counts.get)]


def part1(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards, shifts = get_guards_and_shifts(schedule_log)
    sleepiest_guard = get_sleepiest_guard(guards)
    minute_asleep_most, count = get_sleepiest_minute(sleepiest_guard)
    return sleepiest_guard['ID'] * minute_asleep_most


def part2(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards, shifts = get_guards_and_shifts(schedule_log)
    guard_most_frequently_asleep_on_same_minute = get_guard_most_frequently_asleep_on_same_minute(guards)
    return (guard_most_frequently_asleep_on_same_minute['ID'] *
            get_sleepiest_minute(guard_most_frequently_asleep_on_same_minute)[0])
