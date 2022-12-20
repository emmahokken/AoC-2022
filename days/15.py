import re
from tqdm import tqdm
import numpy as np

from utils.read_file import read_file, read_test_file

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Distress():
    def __init__(self, xs, ys, xb, yb):
        self.sensor = Point(xs, ys)
        self.beacon = Point(xb, yb)
        self.dist = manhattan_distance(self.sensor, self.beacon)

    def __repr__(self):
        # return f'{self.sensor}'
        return f'Sensor at {self.sensor}: closest beacon is at {self.beacon}, the distance is {self.dist}\n'

    # def manhattan_distance(self, a,b):
    #     return abs(a.x - b.x) + abs(a.y - b.y)
    #

def manhattan_distance(a,b):
        return abs(a.x - b.x) + abs(a.y - b.y)

def place_beacons(locs, Y):
    no_beacons_possible = set()

    # go over each pair
    for loc in tqdm(locs):
        s = loc.sensor
        b = loc.beacon
        d = loc.dist
        for i in range(-d, d+1):
            f = abs(abs(i) - d)
            yy = s.y + i
            if yy == Y:
                for pt in range(s.x - f, s.x + f + 1):
                    if (b.x, b.y) != (pt, yy):
                        no_beacons_possible.add(pt)
    return len(no_beacons_possible)

def find_distress_beacon(locs, threshold):
    no_beacons_possible = set()

    # go over each pair
    for loc in tqdm(locs):
        s = loc.sensor
        b = loc.beacon
        d = loc.dist
        for i in range(-d, d+1):
            f = abs(abs(i) - d)
            yy = s.y + i
            for xx in range(s.x - f, s.x + f + 1):
                if (b.x, b.y) != (xx, yy) and xx <= threshold and yy <= threshold and xx >= 0 and yy >= 0:
                    no_beacons_possible.add((xx, yy))
    return no_beacons_possible

def main():
    lines = read_test_file(day=15)

    threshold = 20
    locs = []
    locs_reduced = []
    sensor_coords = set()
    for line in lines:
        _, x0, _, y0, _, x1, _, y1 = re.split('x=|y=|,|:', line)
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        locs.append(Distress(x0, y0, x1, y1))
        # if x0 <= threshold and y0 <= threshold and x1 <= threshold and y1 <= threshold \
        #         and x0 >= 0 and y0 >= 0 and x1 >= 0 and y1 >= 0:
        #     locs_reduced.append(Distress(x0, y0, x1, y1))
        sensor_coords.add((x0, x1))


    Y_test = 10
    Y = 2000000
    # count = place_beacons(locs, Y)
    # print(f'Part 1: On row {Y}, {count} places cannot contain a beacon')

    Y_big_test = 20
    Y_big = 4000000

    # compare = set()
    # for i in tqdm(range(Y_big)):
    #     print('jkl')
    #     for j in range(Y_big):
    #         compare.add((i,j))

    places_beacon_cannot_be = find_distress_beacon(locs, Y_big_test)
    #
    print(places_beacon_cannot_be - sensor_coords)

    exit()
    places_without_beacon = compare - all_places
    places_without_beacon = places_without_beacon - sensor_coords
    print(places_without_beacon)

    exit()

    # x_s = []
    # y_s = []
    # locs.append(d)
    # x_s.append(x0)
    # x_s.append(x1)
    # y_s.append(y0)
    # y_s.append(y1)

    print(locs)

    grid = np.zeros(())
    print(min(x_s), max(x_s), min(y_s), max(y_s))

    grid = {(i, j): 0 for i in range(min(x_s), max(x_s)) for j in range(min(y_s), max(y_s))}


    for loc in locs:
        between_x = [x for x in range(loc.sensor[0], loc.beacon[0])]
        if len(between_x) == 0:
            between_x = [x for x in range(loc.beacon[0], loc.sensor[0])]

        between_y = [x for x in range(loc.sensor[1], loc.beacon[1])]
        if len(between_y) == 0:
            between_y = [x for x in range(loc.beacon[1], loc.sensor[1])]

        for x, y in zip(between_x, between_y):
            grid[(x,y)] = 1

    for xf in grid.values():
        if xf == 1:
            print(xf)



if __name__ == '__main__':
    main()