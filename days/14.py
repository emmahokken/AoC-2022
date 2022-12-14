import copy
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from utils.read_file import read_file, read_test_file


def let_sand_fall(cave, i):
    sand_starter_pos = (500, 0)
    down_x, down_y = 0, 1
    left_x, left_y = -1, 1
    right_x, right_y = 1, 1

    i += 1
    moved = True
    curr_x, curr_y = sand_starter_pos
    while moved:
        if curr_y + down_y < cave.shape[0] and curr_x + down_x < cave.shape[1] and cave[
            curr_y + down_y, curr_x + down_x] == 0:
            # move down
            curr_x += down_x
            curr_y += down_y
            continue
        elif curr_y + left_y < cave.shape[0] and curr_x + left_x < cave.shape[1] and cave[
            curr_y + left_y, curr_x + left_x] == 0:
            # move left
            curr_x += left_x
            curr_y += left_y
            continue
        elif curr_y + right_y < cave.shape[0] and curr_x + right_x < cave.shape[1] and cave[
            curr_y + right_y, curr_x + right_x] == 0:
            # move right
            curr_x += right_x
            curr_y += right_y
            continue

        # we've reached the bottom
        cave[curr_y, curr_x] = 1
        moved = False

    return cave, i

def main():
    '''
    air = 0
    sand = 1
    rock = 2

    562 too low
    656 too high
    it was fucking 655

    2863 too low
    2864 too low
    it's 26484 sooooooo... yeah, too low
    '''
    lines = read_file(day=14)

    rc = np.zeros((250,800))

    # parse file
    my = []
    for line in lines:
        line_cords = []
        coords = line.split('->')
        for i, c in enumerate(coords):
            x,y = c.split(',')
            cord = (int(x), int(y))
            my.append(int(y))
            line_cords.append(cord)
            if len(line_cords) > 1:
                (x0, y0), (x1, y1) = sorted([cord, line_cords[i-1]])
                rc[y0:y1+1,x0:x1+1] = 2


    rc[max(my)+2, :] = 2
    cave = np.array(copy.deepcopy(rc[:max(my)+3,:]))

    i = 0
    cave_through_time = [list(cave)]

    # go down the drain (up, in this case)
    while not 1 in cave[cave.shape[0] - 2]:
        cave, i = let_sand_fall(cave, i)
        # cave_through_time.append(list(cave))

    print(f'Part 1: The sand will fall infinitely after sand block {i-1}')

    i = 0
    cave = np.array(copy.deepcopy(rc[:max(my)+3,:]))
    cave_through_time = [copy.deepcopy(cave)]

    while cave[0, 500] != 1:
        cave, i = let_sand_fall(cave, i)
        cave_through_time.append(copy.deepcopy(cave))

    print(f'Part 2: The sand will reach the top after sand block {i}')
    # print(rc[0:10,494:504])
    animate_sand(cave_through_time, cave.shape[0])

def animate_sand(cave_through_time, shape):
    dip, dap = 400, 620
    fig = plt.figure(figsize=(10,10))
    plt.axis('off')
    im = plt.imshow(cave_through_time[0][:shape, dip:dap])
    fig.suptitle(f'Sand status after sand block {0}')

    def animate_func(i):
        im.set_array(cave_through_time[i][:shape, dip:dap])
        fig.suptitle(f'Sand status after sand block {i}')
        return [im]

    anim = animation.FuncAnimation(fig, animate_func, frames=len(cave_through_time), interval=1000/200)

    anim.save('../output/big_big_test.mp4')

if __name__ == '__main__':
    main()