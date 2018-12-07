import datetime

from collections import defaultdict


def parse_date(log_line):
    date_string = log_line[log_line.index('[') + 1:log_line.index(']')]
    return datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')


def get_guard_number(log_line):
    guard_fh = log_line[log_line.index('#') + 1:]
    return int(guard_fh[:guard_fh.index(' ')])


def get_guards(schedule_log):
    guards = {}
    current_guard = None
    sleep_start = None
    for log_line in schedule_log:
        if "Guard" in log_line:
            guard_number = get_guard_number(log_line)
            if guard_number not in guards:
                guards[guard_number] = []
            current_guard = guards[guard_number]
        if 'sleep' in log_line:
            sleep_start = parse_date(log_line).minute
        if 'wake' in log_line:
            current_guard.append(range(sleep_start, parse_date(log_line).minute))
    return guards


def get_total_sleep(sleep_ranges):
    return sum(len(sleep) for sleep in sleep_ranges)


def get_sleepiest_guard(guards):
    return max(guards, key=sum)


def get_minutes_slept(sleep_ranges):
    minutes_slept = defaultdict(int)
    for sleep in sleep_ranges:
        for minute in sleep:
            minutes_slept[minute] += 1
    return minutes_slept


def get_sleepiest_minute(sleep_ranges):
    minutes_slept = get_minutes_slept(sleep_ranges)
    minute = max(minutes_slept, key=minutes_slept.get)
    return minute, minutes_slept[minute]


def get_guard_most_frequently_asleep_on_same_minute(guards):
    sleepiest_minute_counts = {guard: get_sleepiest_minute(sleep_ranges)[1] for guard, sleep_ranges in guards.items() if
                               len(sleep_ranges) > 0}
    return max(sleepiest_minute_counts, key=sleepiest_minute_counts.get)


def part1(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards = get_guards(schedule_log)
    sleepiest_guard = max(guards, key=lambda x: get_total_sleep(guards[x]))
    minute_asleep_most, count = get_sleepiest_minute(guards[sleepiest_guard])
    return sleepiest_guard * minute_asleep_most


def part2(day4_input):
    schedule_log = sorted(day4_input.splitlines())
    guards = get_guards(schedule_log)
    guard_most_frequently_asleep_on_same_minute = get_guard_most_frequently_asleep_on_same_minute(guards)
    sleepiest_minute_of_guard = get_sleepiest_minute(guards[guard_most_frequently_asleep_on_same_minute])[0]
    return guard_most_frequently_asleep_on_same_minute * sleepiest_minute_of_guard
