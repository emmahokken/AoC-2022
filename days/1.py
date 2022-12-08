from utils.read_file import read_file

def main():
    calories = read_file(day=1)

    elves = [0]
    idx = 0 
    for cal in calories:
        if cal != '':
            elves[idx] += int(cal) 
        elif cal == '':
            elves.append(0)
            idx += 1

    elves.sort(reverse=True)

    print(f'Part 1: The Elf carrying the post calories is carrying {elves[0]} calories')
    print(f'Part 2: The top three Elves are carrying {sum(elves[:3])} calories')


if __name__ == '__main__':
    main()