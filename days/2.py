def read_file(day):
    with open(f'../input/{day}.txt', 'r') as f:
        lines = []
        for line in f:
            game = line.strip().split(' ')
            lines.append({'you': game[0], 'me': game[1]})
        return lines

def main():
    games = read_file(day=2)
    points = [
        [1+0, 1+3, 1+6],
        [2+0, 2+3, 2+6],
        [3+0, 3+3, 3+6],
    ]

    total_points_1 = 0
    total_points_2 = 0

    for game in games:
        # part 1
        if game['you'] == 'A':
            if game['me'] == 'X':
                total_points_1 += points[0][1]
            elif game['me'] == 'Y':
                total_points_1 += points[1][2]
            elif game['me'] == 'Z':
                total_points_1 += points[2][0]
        elif game['you'] == 'B':
            if game['me'] == 'X':
                total_points_1 += points[0][0]
            elif game['me'] == 'Y':
                total_points_1 += points[1][1]
            elif game['me'] == 'Z':
                total_points_1 += points[2][2]
        if game['you'] == 'C':
            if game['me'] == 'X':
                total_points_1 += points[0][2]
            elif game['me'] == 'Y':
                total_points_1 += points[1][0]
            elif game['me'] == 'Z':
                total_points_1 += points[2][1]

        # part 2
        if game['you'] == 'A':
            if game['me'] == 'X':
                total_points_2 += points[2][0]
            elif game['me'] == 'Y':
                total_points_2 += points[0][1]
            elif game['me'] == 'Z':
                total_points_2 += points[1][2]
        elif game['you'] == 'B':
            if game['me'] == 'X':
                total_points_2 += points[0][0]
            elif game['me'] == 'Y':
                total_points_2 += points[1][1]
            elif game['me'] == 'Z':
                total_points_2 += points[2][2]
        elif game['you'] == 'C':
            if game['me'] == 'X':
                total_points_2 += points[1][0]
            elif game['me'] == 'Y':
                total_points_2 += points[2][1]
            elif game['me'] == 'Z':
                total_points_2 += points[0][2]

    print(f'Part 1: After all games you have {total_points_1} points')        
    print(f'Part 2: With the new format and after all games you have {total_points_2} points')

if __name__ == '__main__':
    main()