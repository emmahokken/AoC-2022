from utils.read_file import read_file
import math 
import numpy as np 

def main():

    directions = {'L': [-1,0], 'R': [1,0], 'U': [0,1], 'D': [0,-1]}
    places = set()
    other_places = set()
    knots = np.zeros((10,2))

    for line in read_file(day=9):
        dir, steps = line.split()
        steps = int(steps)

        # for each step 
        for _ in range(steps):
            knots[0] = np.add(knots[0], directions[dir])
                
            for i in range(1, len(knots)):      
                prev_k = knots[i-1]
                if math.dist(prev_k, knots[i]) >= 2:
                    knots[i] += np.sign(prev_k - knots[i])  
            
            places.add((knots[1][0], knots[1][1]))
            other_places.add((knots[9][0], knots[9][1]))
                

    print(f'Part 1: The tail stops at {len(places)} places')
    print(f'Part 2: The tail stops at {len(other_places)} places')
    
if __name__ == '__main__':
    main()