from utils.read_file import read_file

def main():
    lines = read_file(day=4)

    contained_part1 = 0
    contained_part2 = 0
    for line in lines:
        pair1, pair2 = line.split(',')

        pair1 = [int(x) for x in pair1.split('-')]
        pair2 = [int(x) for x in pair2.split('-')]
        
        if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
            contained_part1 += 1 
        elif pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
            contained_part1 += 1 

        pair1 = [int(x) for x in range(int(pair1[0]), int(pair1[1])+1)]
        pair2 = [int(x) for x in range(int(pair2[0]), int(pair2[1])+1)]
        
        common = set(pair1) & set(pair2)
        if len(common) > 0:
            contained_part2 += 1        

    print(f'Part 1: The total number of overlapping tasks is {contained_part1}')
    print(f'Part 2: The total number of partially overlapping tasks is {contained_part2}')

if __name__ == '__main__':
    main()