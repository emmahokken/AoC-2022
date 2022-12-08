from collections import defaultdict

class Node():
    def __init__(self, name, is_file=False, size=None, parent=None):
        self.name = name
        self.children = {}
        self.size = size
        self.parent = parent
        self.is_file = is_file

    def add_child(self, content):
        assert isinstance(content, Node)
        self.children[content.name] = content

    def __str__(self):
        return f'Node named {self.name} with children {self.children}'

    def __repr__(self):
        if self.is_file:
            return f'File named {self.name} of size {self.size}'
        return f'Node named {self.name} with children {self.children}'


def read_file(day):
    with open(f'../input/{day}.txt', 'r') as f:
        return f.read().splitlines()

def main():
    lines = read_file(day=7)

    root = Node('/')
    working_dir = root

    for line in lines:
        line = line.split(' ')
        if line[0] == '$':
            if line[1] == 'cd':
                *_, name = line
                if name == '/':
                    working_dir = root
                elif name != '..':
                    if name not in working_dir.children.keys():
                        working_dir.add_child(Node(name=name))
                    working_dir = working_dir.children[name]
                elif name == '..':
                    working_dir = working_dir.parent
        elif line[0].isdigit():
            size, name = line
            node = Node(name=name, size=int(size), parent=working_dir, is_file=True)
            working_dir.add_child(node)
        elif line[0] == 'dir':
            _, name = line
            node = Node(name=name, parent=working_dir)
            working_dir.add_child(node)

    overall_size, sizes = calc_sum(root, [])
    final = sum(filter(lambda x: x < 100000, sizes))
    print(f'Part 1: total size of directories under 100000 is {final}')

    total_disk_space = 70000000
    needed_disk_space = 30000000

    needed = needed_disk_space - (total_disk_space - overall_size)
    final = min(filter(lambda x: x > needed, sizes))
    print(f'Part 2: The smallest directory to delete that will free up enough space has a size of {final}')

def calc_sum(node, sizes):
    if node.is_file:
        return node.size, sizes
    sizes.append(sum(calc_sum(child, sizes)[0] for child in node.children.values()))
    return sizes[-1], sizes


if __name__ == '__main__':
    main()