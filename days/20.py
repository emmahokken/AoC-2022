import numpy as np
from utils.read_file import read_file, read_test_file

def mix(coords, orig_coords, coords_len):
    for c in orig_coords:
        i = coords.index(c)

        value, idx = c
        # new index
        new_i = (i + value) % (coords_len - 1)
        if new_i == 0:
            new_i = coords_len - 1

        coords.pop(i)
        coords.insert(new_i, c)

    return coords

def main():
    coords = [(int(line),i) for i, line in enumerate(read_file(day=20))]
    orig_coords = [(int(line),i) for i, line in enumerate(read_file(day=20))]
    coords_len = len(coords)

    coords = mix(coords, orig_coords, coords_len)
    mixed_coords = [c[0] for c in coords]

    # find 0 index
    z_idx = mixed_coords.index(0)

    # now find 1000th, 2000th, and 3000th value after 0
    ctw = [mixed_coords[(z_idx + i) % coords_len] for i in range(1000, 3001, 1000)]

    print(f'Part 1: the sum of the 1000th, 2000th, and 3000th numbers after mixing is {sum(ctw)}')

    encryption_key = 811589153
    coords = [(int(line) * encryption_key, i) for i, line in enumerate(read_file(day=20))]
    orig_coords = [(int(line) * encryption_key, i) for i, line in enumerate(read_file(day=20))]

    for _ in range(10):
        coords = mix(coords, orig_coords, coords_len)

    mixed_coords = [c[0] for c in coords]
    z_idx = mixed_coords.index(0)
    ctw = [mixed_coords[(z_idx + i) % coords_len] for i in range(1000, 3001, 1000)]
    print(f'Part 2: the sum of the 1000th, 2000th, and 3000th numbers after mixing is {sum(ctw)}')

if __name__ == '__main__':
    main()