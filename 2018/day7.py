import re

from collections import defaultdict


seconds_per_step = 60
worker_count = 5


def get_available_steps(steps):
    counts = defaultdict(int)
    for step, dependencies in steps.items():
        for dependency in dependencies:
            counts[dependency] += 1
    return [dependency for dependency in steps if counts[dependency] == 0]


def part1(steps_input):
    steps = get_steps(steps_input.strip().splitlines())
    step_order = []
    while len(steps) > 0:
        available_steps = sorted(get_available_steps(steps))
        selected = min(available_steps)
        step_order.append(selected)
        steps.pop(selected)
    return ''.join(step_order)


def get_total_time(step):
    return ord(step) - 64 + seconds_per_step


def get_steps(step_instructions):
    steps = {}
    for instruction in step_instructions:
        prereq, step = re.search('Step ([A-Z]) must be finished before step ([A-Z]) can begin.', instruction).groups()
        if prereq not in steps:
            steps[prereq] = []
        if step not in steps:
            steps[step] = []
        steps[prereq].append(step)
    return steps


def part2(steps_input):
    # steps is a graph implemented with a simple dictionary used for a directed acyclic graph vertex: edge list
    steps = get_steps(steps_input.strip().splitlines())

    current_jobs = {}
    available_steps = get_available_steps(steps)
    total_time = 0
    while len(available_steps) > 0:
        # assign jobs
        for step in sorted(available_steps):
            if len(current_jobs) < worker_count and step not in current_jobs:
                current_jobs[step] = get_total_time(step)
        # do work
        time_worked = min(current_jobs.values())
        for job, time_left in current_jobs.copy().items():
            if time_left == time_worked:
                steps.pop(job)
                current_jobs.pop(job)
            else:
                current_jobs[job] -= time_worked

        total_time += time_worked
        available_steps = get_available_steps(steps)
    return total_time


def test():
    test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

    global seconds_per_step, worker_count
    twc = worker_count
    worker_count = 2
    tsps = seconds_per_step
    seconds_per_step = 0
    assert part1(test_input) == 'CABDFE'
    assert part2(test_input) == 15
    seconds_per_step = tsps
    worker_count = twc


if __name__ == '__main__':
    test()
