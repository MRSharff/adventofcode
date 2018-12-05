from collections import defaultdict
from itertools import combinations


def get_letter_counts(box_id):
    counts = defaultdict(int)
    for char in box_id:
        counts[char] += 1
    return counts


def checksum(box_ids):
    two_count = 0
    three_count = 0
    for box_id in box_ids:
        letter_counts = get_letter_counts(box_id).values()
        if 2 in letter_counts:
            two_count += 1
        if 3 in letter_counts:
            three_count += 1
    return two_count * three_count


def get_differences(str1, str2):
    differences = {}
    for i, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            differences[i] = (char1, char2)
    return differences


def get_prototype_boxes(candidate_ids):
    for id1, id2 in combinations(candidate_ids, 2):
        differences = get_differences(id1, id2)
        if len(differences) == 1:
            return id1, id2


def common_characters(str1, str2):
    return ''.join([a for a, b in zip(str1, str2) if a == b])


def part1(day2input):
    likely_candidates = day2input.splitlines()
    return checksum(likely_candidates)


def part2(day2input):
    likely_candidates = day2input.splitlines()
    return common_characters(*get_prototype_boxes(likely_candidates))
