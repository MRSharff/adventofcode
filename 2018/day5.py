import string

def annihilates(unit1, unit2):
    return abs(ord(unit1) - ord(unit2)) == 32


def react(polymer):
    catalyzed_polymer = []
    for unit in polymer:
        if catalyzed_polymer and annihilates(catalyzed_polymer[-1], unit):
            catalyzed_polymer.pop()
        else:
            catalyzed_polymer.append(unit)
    return ''.join(catalyzed_polymer)


def remove_all(unit, polymer):
    return polymer.replace(unit, '').replace(unit.upper(), '')


def tests():
    test_polymer = 'dabAcCaCBAcCcaDA'

    assert react(test_polymer) == 'dabCBAcaDA'

    assert react('aA') == ''
    assert react('abBA') == ''
    assert react('abAB') == 'abAB'
    assert react('aabAAB') == 'aabAAB'

    assert part1(test_polymer) == 10

    assert remove_all('a', test_polymer) == 'dbcCCBcCcD'
    assert remove_all('b', test_polymer) == 'daAcCaCAcCcaDA'
    assert remove_all('c', test_polymer) == 'dabAaBAaDA'
    assert remove_all('d', test_polymer) == 'abAcCaCBAcCcaA'

    assert react(remove_all('a', test_polymer)) == 'dbCBcD'
    assert react(remove_all('b', test_polymer)) == 'daCAcaDA'
    assert react(remove_all('c', test_polymer)) == 'daDA'
    assert react(remove_all('d', test_polymer)) == 'abCBAc'

    assert part2(test_polymer) == 4

    print("tests successful")


def part1(polymer):
    return len(react(polymer))


def part2(polymer):
    unit_types = string.ascii_lowercase
    polymer_sizes = [len(react(remove_all(unit, polymer))) for unit in unit_types]
    return min(polymer_sizes)


if __name__ == '__main__':
    tests()
