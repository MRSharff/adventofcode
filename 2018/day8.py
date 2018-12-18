class Node:

    def __init__(self, license_iter) -> None:
        super().__init__()
        self.child_count = next(license_iter)
        self.metadata_count = next(license_iter)
        self.child_nodes = [Node(license_iter) for _ in range(self.child_count)]
        self.metadata = [next(license_iter) for _ in range(self.metadata_count)]


class Tree:

    def __init__(self, license_file) -> None:
        super().__init__()
        self.root = Node(iter(int(d) for d in license_file.split(' ')))


def node_value(node):
    if node.child_count == 0:
        return sum(node.metadata)
    else:
        return sum(0 if index - 1 >= len(node.child_nodes) else node_value(node.child_nodes[index - 1])
                   for index in node.metadata)


def checksum(node):
    if node.child_count == 0:
        return sum(node.metadata)
    else:
        return sum(checksum(n) for n in node.child_nodes) + sum(node.metadata)


def part1(license_file):
    return checksum(Tree(license_file).root)


def part2(license_file):
    return node_value(Tree(license_file).root)


def tests():
    test_license_file = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    assert part1(test_license_file) == 138
    assert part2(test_license_file) == 66


if __name__ == '__main__':
    tests()
