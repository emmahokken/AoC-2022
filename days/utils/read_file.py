def read_file(day):
     with open(f'../input/{day}.txt', 'r') as f:
        return f.read().splitlines()

def read_test_file(day):
    with open(f'../input/{day}_test.txt', 'r') as f:
        return f.read().splitlines()
