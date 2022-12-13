import numpy as np
import math
from utils.read_file import read_file, read_test_file

def calc_score(curr, end):
    return math.dist(curr, end)

def find_valid_moves(grid, i, j, part):
    options = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]

    if part == 1:
        return [op for op in options if 0 <= op[0] < grid.shape[0]
                                   and 0 <= op[1] < grid.shape[1]
                                   and (grid[op] - grid[i,j]) < 2]

    return [op for op in options if 0 <= op[0] < grid.shape[0]
            and 0 <= op[1] < grid.shape[1]
            and (grid[i, j] - grid[op]) < 2]

def hill_climbing(grid, start_state, end_state, part):
    # remember possible options to visit
    to_visit = [{'state': start_state, 'cost': 0}]
    visited = set()

    while len(to_visit) > 0:
        # pop first entry from to_visit
        working = to_visit.pop(0)

        state = working['state']
        cost = working['cost']

        # only go to space if not yet visited
        if state in visited:
            continue
        visited.add(state)
        i, j = state

        if state in set(end_state):
            return cost

        # explore next options
        valid_moves = find_valid_moves(grid, i, j, part=part)
        for op in valid_moves:
            to_visit.append({'state': op, 'cost': cost+1})

def main():
    lines = read_file(day=12)

    start = ord('S')
    end = ord('E')
    grid = np.empty((len(lines), len(lines[0])))

    # parse file
    for i, line in enumerate(lines):
        int_lines = [ord(l) for l in line]
        grid[i] = np.array(int_lines)

    # get coordinates of start and end state
    start_state = np.where(grid == start)
    end_state = np.where(grid == end)

    start_state = (start_state[0][0], start_state[1][0])
    end_state = (end_state[0][0], end_state[1][0])
    en = set()
    en.add(end_state)

    # make start and end state usable
    grid[start_state] = ord('a')
    grid[end_state] = ord('z')


    print(f'Part 1: The shortest possible path from S to E contains {hill_climbing(grid, start_state, en, part=1)} steps')

    end_states = np.where(grid == ord('a'))
    end_states = [(x,y) for x,y in zip(end_states[0], end_states[1])]

    print(f'Part 2: The shortest possible path from any S to E contains {hill_climbing(grid, end_state, end_states, part=2)} steps')

if __name__ == '__main__':
    main()