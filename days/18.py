import numpy as np
import matplotlib.pyplot as plt
from utils.read_file import read_file, read_test_file

def main():
    lines = read_test_file(day=18)
    cubes = []
    cubes_mat = []
    for line in lines:
        l = line.split(',')
        cubes.append(tuple([int(i) for i in l]))
        cubes_mat.append([int(i) for i in l])

    cubes_mat = np.array(cubes_mat)
    neighbour_coords = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
    total_sides = 6 * len(cubes)

    for cube in cubes:
        for neighbour in neighbour_coords:
            nc = tuple([sum(x) for x in zip(cube, neighbour)])
            if nc in cubes:
                total_sides -= 1

    print(f'Part 1: The total surface area is {total_sides}')

    print(cubes_mat.shape)
    maxx = np.amax(cubes_mat, axis=0)
    maxy = np.amax(cubes_mat, axis=1)
    print(maxx, maxy)
    # exit()

    # print(cubes)
    data = [np.ones(cube) for cube in cubes_mat]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    for d in data:
        ax.voxels(d, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()