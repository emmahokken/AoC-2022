from utils.read_file import read_file

def convert(letter):
    if letter.isupper():
        return ord(letter) - 65 + 26 + 1
    elif letter.islower():
        return ord(letter) - 97 + 1

def main():
    lines = read_file(day=3)
    score = 0

    for line in lines:
        l = int(len(line) / 2)
        part1 = list(line[:l])
        part2 = list(line[l:])

        common = set(part1) & set(part2)
        score += convert(common.pop())

    print(f'Part 1: The score is {score}')

    score = 0
    n = 3

    for g in range(n, len(lines) + 1, n):            
        group = lines[g-n:g]
        common = set(group[0]) & set(group[1]) & set(group[2])
        score += convert(common.pop())
    
    print(f'Part 2: The score is {score}')
   
if __name__ == '__main__':
    main()