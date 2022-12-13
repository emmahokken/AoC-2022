import ast
import numpy as np

from functools import cmp_to_key

from utils.read_file import read_file_double_whiteline, read_test_file_double_whiteline

class Pair():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'This pair consists of left {self.left} and right {self.right}\n'

def find_shortest_end(left, right):
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            # if value left < value right -> right order
            if l < r:
                return 1
            # if value left > value right -> wrong order
            elif l > r:
                return -1

        # make sure both sides are list
        if isinstance(l, list) and isinstance(r, int):
            r = [r]
        elif isinstance(l, int) and isinstance(r, list):
            l = [l]

        # if both values are lists
        if isinstance(l, list) and isinstance(r, list):
            # go deeper
            deep_find = find_shortest_end(l, r)
            # if no solution was found, continue to next list
            if deep_find == 0:
                continue
            # if a solution was found, return it
            return deep_find

    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1

    # no condition was met
    return 0

def guess_ill_do_fucking_bubble_sort(to_sort):

    print(to_sort)
    n = len(to_sort)
    contains_list = [i for i, el in enumerate(to_sort) if isinstance(el, list)]

    for sub_list in contains_list:
        return guess_ill_do_fucking_bubble_sort(to_sort[sub_list])

    while True:
        swapped = False
        for i in range(1, n):
            if to_sort[i-1] < to_sort[i]:
                tmp = to_sort[i-1]
                to_sort[i-1] = to_sort[i]
                to_sort[i] = tmp
                swapped = True

        if not swapped:
            break

    return to_sort

def recursive_sort(to_sort):
    print(f'We are gonna sort {to_sort}')

    # check if list contains list
    contains_list = [i for i, el in enumerate(to_sort) if isinstance(el, list)]
    print(f'Go deeper for indices {contains_list}')

    # if there are no deeper lists -> return current one
    if len(contains_list) == 0:
        print('we are returning', to_sort)
        return to_sort

    # if first item in list is not a list but int, sort based on that int
    if contains_list[0] != 0:
        print('first item is not a list, so return', to_sort)
        return [to_sort[0]]

    for sub_list in contains_list:
        return recursive_sort(to_sort[sub_list])

def main():
    lines = read_file_double_whiteline(day=13)

    pairs = []
    for line in lines:
        left, right = line.split('\n')
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        pairs.append(Pair(left=left, right=right))

    ordered = [find_shortest_end(pair.left, pair.right) for pair in pairs]
    ordered_sum = sum(i + 1 for i, x in enumerate(ordered) if x > 0)
    print(f'Part 1: The sum of the indices of the signals in the right order is {ordered_sum}')

    to_sort_packets = []
    for pair in pairs:
        to_sort_packets.append(pair.left)
        to_sort_packets.append(pair.right)
   
    to_sort_packets.append([[2]])
    to_sort_packets.append([[6]])

    sorted_packets = sorted(to_sort_packets, key=cmp_to_key(find_shortest_end), reverse=True)
    indices = sorted_packets.index([[2]]) * sorted_packets.index([[6]])
    print(f'Part 2: The product of the indices of the two distress signals is {indices}')

    # i wish the below thing worked :(
    # sorted_packets = sorted(to_sort_packets, key=recursive_sort)

    
if __name__ == '__main__':
    main()


