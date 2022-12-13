from utils.read_file import read_file
import numpy as np

def main():
    program = read_file(day=10)
    X = 1
    x = [X]
    interesting_cycles = [x for x in range(20, 250, 40)]
    cycle_sum = 0
    
    for line in program:
        prog = line.split(' ')

        # if noop, do nothing, just append current X 
        if prog[0] == 'noop':
            x.append(X)

        # addx takes two cycles, so add X before and after increasing 
        elif prog[0] == 'addx':
            x.append(X)
            X += int(prog[1])
            x.append(X)

    
    cycle_sum = sum([i*x[i-1] for i in interesting_cycles])
    print(f'Part 1: The sum of the signal strengths of the interesting cycles is {cycle_sum}')

    lit = '#'
    dark = ' '
    grid = np.full((6,40), dark, dtype=str)
    l = 39

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            sprite_loc = x[row+col+(row*l)] 
            if abs(col - sprite_loc) < 2:
                grid[row, col] = lit

    print('Part 2: The CRT produces the following letters')
    for i in range(grid.shape[0]):
        print(''.join(grid[i]))
    print('PAPJCBHP')

if __name__ == '__main__':
    main()