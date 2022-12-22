import numpy as np
import re

from utils.read_file import read_file_double_whiteline


def main():
    board, instructions = read_file_double_whiteline(day=22)
    test_width = 16
    # clean up board
    board = board.split('\n')
    board_rep = []
    for line in board:
        twi = np.zeros(len(board[0]))
        for i, c in enumerate(line):
            if c == '.':
                twi[i] = 1
            elif c == '#':
                twi[i] = 2

        board_rep.append(twi)
    board = np.array(board_rep)

    # clean up instructions
    instructions = re.split('(\d+)', instructions)
    for i, inst in enumerate(instructions):
        if inst.isdigit():
            instructions[i] = int(inst)
    instructions = instructions[:-1]

    # facing array (right = 3, down = 4, left = 5, up is 6)
    facings = [3, 4, 5, 6]
    f_idx = 0
    ones = np.where(board[0] != 0)
    curr_pos = (0,ones[0][0])
    max_x, max_y = board.shape
    # now the real thing
    for inst in instructions:
        if isinstance(inst, int):
            x, y = curr_pos
            # go forward n steps
            if facings[f_idx] == 3: # right
                new_y = y+inst
                if new_y > max_y:

                ones = np.where(board[] != 0)
                stretch = board[x, y:(y+inst)%max_y]
                for i in stretch:
                    if i == 2:
                        continue
                    y += 1  # might be needed before if
            elif facings[f_idx] == 4: # down
                stretch = board[x:(x+inst)%max_x,y]
                for i in stretch:
                    if i == 2:
                        continue
                    x += 1
            elif facings[f_idx] == 5: # left
                stretch = board[(x-inst)%max_x:x,y]
                for i in stretch:
                    if i == 2:
                        continue
                    x -= 1
            elif facings[f_idx] == 5:  # left
                stretch = board[x, (y-inst)%max_y:y]
                for i in stretch:
                    if i == 2:
                        continue
                    y -= 1

            curr_pos = (x,y)
        elif inst == 'L':
            print('l')
            f_idx = (f_idx - 1) % len(facings)
        elif inst == 'R':
            print('r')
            f_idx = (f_idx + 1) % len(facings)


    print(curr_pos)








if __name__ == '__main__':
    main()