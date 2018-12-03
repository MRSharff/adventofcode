from collections import defaultdict

import advent_of_code

def get_letter_counts(box_id):
    counts = defaultdict(int)
    for char in box_id:
        counts[char] += 1
    return counts

def get_likely_candidates():
    return advent_of_code.get_day_input(2).splitlines()

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

if __name__ == '__main__':
    print(checksum(get_likely_candidates()))
