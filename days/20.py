import numpy as np
from utils.read_file import read_file, read_test_file

class Coord():
    def __init__(self, value, moved=False):
        self.value = value
        self.moved = moved

    def __repr__(self):
        return f'{self.value}'
        return f'{self.value}: {self.moved}'

def any_moves_left(coords):
    for coord in coords:
        if not coord.moved:
            return True
    return False

def coord_to_move(coords):
    for i, coord in enumerate(coords):
        if not coord.moved:
            return i, coord

    return False

def find_zero(coords):
    for i, c in enumerate(coords):
        if c.value == 0:
            return i

def mix(coords, coords_len):
    while any_moves_left(coords):
        # find the first number that has not been moved yet
        i, c = coord_to_move(coords)
        # new index
        new_i = (i + c.value) % (coords_len - 1)
        if new_i == 0:
            new_i = coords_len - 1

        print(f'We are moving {c.value}, from index {i}, to index {new_i}')

        coords = np.delete(coords, i)
        coords = np.insert(coords, new_i, Coord(c.value, moved=True))

    return coords

def main():
    '''
    -102 wrong
    -12110 wrong
    2622 right!
    '''

    coords = np.array([Coord(int(line)) for line in read_file(day=20)])
    coords_len = len(coords)
    coords = mix(coords, coords_len)

    # find 0 index
    z_idx = find_zero(coords)

    # now find 1000th, 2000th, and 3000th value after 0
    ctw = [coords[(z_idx + i) % coords_len].value for i in range(1000, 3001, 1000)]

    print(f'Part 1: the sum of the 1000th, 2000th, and 3000th numbers after mixing is {sum(ctw)}')

    encryption_key = 811589153

    coords = np.array([Coord(int(line)*encryption_key) for line in read_file(day=20)])


if __name__ == '__main__':
    main()