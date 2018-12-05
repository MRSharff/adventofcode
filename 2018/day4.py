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
    return {'ID': guard_number, 'sleep_times': []}


def get_guards(schedule_log):
    guards = {}
    current_guard = None
    sleep_start = None
    for log_line in schedule_log:
        if "Guard" in log_line:
            guard_number = get_guard_number(log_line)
            if guard_number not in guards:
                guards[guard_number] = make_guard(guard_number)
            current_guard = guards[guard_number]
        if 'sleep' in log_line:
            sleep_start = parse_date(log_line).minute
        if 'wake' in log_line:
            current_guard['sleep_times'].append(range(sleep_start, parse_date(log_line).minute))
    return guards


def get_total_sleep(guard):
    return sum(len(sleep) for sleep in guard['sleep_times'])


def get_sleepiest_guard(guards):
    return max(guards.values(), key=get_total_sleep)


def get_minutes_slept(guard):
    minutes_slept = defaultdict(int)
    for sleep in guard['sleep_times']:
        for minute in sleep:
            minutes_slept[minute] += 1
    return minutes_slept


def get_sleepiest_minute(guard):
    minutes_slept = get_minutes_slept(guard)
    minute = max(minutes_slept, key=minutes_slept.get)
    return minute, minutes_slept[minute]


def get_guard_most_frequently_asleep_on_same_minute(guards):
    sleepiest_minute_counts = {ID: get_sleepiest_minute(guard)[1] for ID, guard in guards.items() if
                               len(guard['sleep_times']) > 0}
    return guards[max(sleepiest_minute_counts, key=sleepiest_minute_counts.get)]


def part1(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards = get_guards(schedule_log)
    sleepiest_guard = get_sleepiest_guard(guards)
    minute_asleep_most, count = get_sleepiest_minute(sleepiest_guard)
    return sleepiest_guard['ID'] * minute_asleep_most


def part2(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards = get_guards(schedule_log)
    guard_most_frequently_asleep_on_same_minute = get_guard_most_frequently_asleep_on_same_minute(guards)
    return (guard_most_frequently_asleep_on_same_minute['ID'] *
            get_sleepiest_minute(guard_most_frequently_asleep_on_same_minute)[0])
