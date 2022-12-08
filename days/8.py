import numpy as np

def read_file(day):
    with open(f'../input/{day}.txt', 'r') as f:
        return f.read().splitlines()

def calc_score(neighbours, tree):
    higher_tree = 0
    for n in neighbours:
        higher_tree += 1
        if n >= tree: break
    return higher_tree

def main():
    trees = np.array([[int(x) for x in l] for l in read_file(day=8)])
    visible_trees = 0
    scores = []

    for i in range(len(trees)):
        for j in range(len(trees[i])):
            tree = trees[i][j]

            left = trees[i, :j]
            right = trees[i, j + 1:]
            up = trees[:i, j]
            down = trees[i + 1:, j]

            if not (
                    any(t >= tree for t in left) and
                    any(t >= tree for t in right) and
                    any(t >= tree for t in up) and
                    any(t >= tree for t in down)
            ):
                visible_trees += 1

            s = [calc_score(reversed(left), tree), calc_score(right, tree), calc_score(reversed(up), tree),
                 calc_score(down, tree)]
            scores.append(np.prod(s))

    print(f'Part 1: The amount of visible trees is {visible_trees}')
    print(f'Part 2: The highest scenic score is {max(scores)}')

if __name__ == '__main__':
    main()