import re

from collections import defaultdict


def claim_coordinates(claim):
    for x in range(int(claim['left_edge']), int(claim['left_edge']) + int(claim['width'])):
        for y in range(int(claim['top_edge']), int(claim['top_edge']) + int(claim['height'])):
            yield x, y


def get_claimed_fabric(claims):
    fabric = defaultdict(int)
    for claim in claims:
        for x, y in claim_coordinates(claim):
            fabric[(x, y)] += 1
    return fabric


def get_overlapping_area_of_claims(fabric):
    return sum(1 for coord in fabric.values() if coord > 1)


def get_claims(day3input):
    r = re.compile('#(?P<ID>\d+) @ (?P<left_edge>\d+),(?P<top_edge>\d+): (?P<width>\d+)x(?P<height>\d+)')
    return [m.groupdict() for m in r.finditer(day3input)]


def claim_overlaps(claim, fabric):
    for x, y in claim_coordinates(claim):
        if fabric[(x, y)] > 1:
            return True
    return False


def get_perfect_claim_id(claims, fabric):
    for claim in claims:
        if not claim_overlaps(claim, fabric):
            return claim['ID']


def part1(day3input):
    day3_claims = get_claims(day3input)
    claimed_fabric = get_claimed_fabric(day3_claims)
    return get_overlapping_area_of_claims(claimed_fabric)


def part2(day3input):
    day3_claims = get_claims(day3input)
    claimed_fabric = get_claimed_fabric(day3_claims)
    return get_perfect_claim_id(day3_claims, claimed_fabric)
