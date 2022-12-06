def read_file(day):
    with open(f'input/{day}.txt', 'r') as f:
        return f.read().splitlines()[0]

def find_start(lines, marker):
    for i in range(len(lines) - marker):
        if len(set(lines[i:i + marker])) == len(lines[i:i + marker]):
            return i + marker

def main():
    lines = read_file(day=6)
    packet_marker = 4
    message_marker = 14

    print(f'Part 1: The start of the first packet marker is located after processing character {find_start(lines, packet_marker)}')
    print(f'Part 2: The start of the first message marker is located after processing character {find_start(lines, message_marker)}')

if __name__ == '__main__':
    main()