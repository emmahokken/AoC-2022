import re
import copy

def read_file():
    with open('../input/5.txt', 'r') as f:
        lines = f.read().split('\n\n')
        return lines[0].split('\n'), lines[1].split('\n')

def main():
    stacks, instructions = read_file()
    neat_stacks = [stack.replace('[','').replace(']', '').replace('    ', ' 2').split(' ') for stack in stacks]
    ordered_stacks = [[neat_stacks[l][i] for l in range(len(neat_stacks) - 1) if neat_stacks[l][i] != '2'] for i in range(len(neat_stacks))]

    neat_instructions = [re.findall(r'\d+', i) for i in instructions]
    neat_instructions = [[int(i), int(j) - 1, int(k) - 1] for i, j, k in neat_instructions]

    stacks_part1 = copy.deepcopy(ordered_stacks)
    stacks_part2 = copy.deepcopy(ordered_stacks)

    for amount, start, end in neat_instructions:
        for _ in range(amount):
            stacks_part1[end].insert(0, stacks_part1[start][0])
            stacks_part1[start].pop(0)

    top_of_stacks = ''.join([stack[0] for stack in stacks_part1])

    print(f'Part 1: The crates at the top of the stacks are: {top_of_stacks}')

    for amount, start, end in neat_instructions:
        stacks_part2[end] = stacks_part2[start][:amount] + stacks_part2[end]
        del stacks_part2[start][:amount]

    top_of_stacks = ''.join([stack[0] for stack in stacks_part2])

    print(f'Part 2: The crates at the top of the stacks are: {top_of_stacks}')

if __name__ == '__main__':
    main()