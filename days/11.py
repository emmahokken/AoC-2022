import operator
import copy 
from tqdm import tqdm

class Monkey():
    def __init__(self, items, op, test, yes, no):
        self.items = items
        self.op = op
        self.test = test
        self.yes = yes
        self.no = no
        self.inspected = 0
        self.test_prod = 1

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def after_inspection(self, item):
        idx = self.get_item(item)
        self.items[idx] //= 3
        return self.items[idx]

    def get_item(self, item):
        idx = operator.indexOf(self.items, item)
        return idx     

    def inspect(self, item, decrease_worry=True):
        self.inspected += 1
        idx = self.get_item(item)
        do, thing = self.op
        if thing == 'old':
            self.items[idx] = (do(self.items[idx], self.items[idx])) 
        else:
            self.items[idx] = (do(self.items[idx], int(thing)))
        
        if not decrease_worry:
            self.items[idx] %= self.test_prod

        return self.items[idx]
        
    def perform_test(self, item):
        return self.yes if item % self.test == 0 else self.no

    def __repr__(self):
        return f'This monkey has items {self.items}, performs op {self.op}, tests if divisible by {self.test}.\n \
            If yes, gives item to monkey {self.yes}. If no, gives item to monkey {self.no}\n'
        
def read_file(day):
     with open(f'../input/{day}.txt', 'r') as f:
        return f.read().split('\n\n')
   
def monkey_business(monkeys, rounds, decrease_worry=True):
    for _ in tqdm(range(rounds)):
        for monkey in monkeys:
            orig_items = copy.deepcopy(monkey.items)
            for item in orig_items:
                # inspect 
                item_inspect = monkey.inspect(item, decrease_worry)
                
                # decrease worry
                item_after_inspect = item_inspect 
                if decrease_worry:
                    item_after_inspect = monkey.after_inspection(item_inspect)
                        
                # test worry level
                give_to = monkey.perform_test(item_after_inspect)
                
                # give item to another monkey
                monkeys[give_to].add_item(item_after_inspect)
                monkey.remove_item(item_after_inspect)
                
    return monkeys

def parse_monkeys(lines):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    test_prod = 1
    monkeys = []
    for m in lines:
        m = m.split('\n')

        items = [int(i[-2:]) for i in m[1].split(',')]
        x = m[2].split(' ')
        op, thing = x[-2:]
        test = int(m[3][-2:])
        yes = int(m[4][-2:])
        no = int(m[5][-2:])

        test_prod *= test
        monkey = Monkey(items=items, op=[ops[op], thing], test=test, yes=yes, no=no)
        monkeys.append(monkey)

    for monkey in monkeys:
        monkey.test_prod = test_prod

    return monkeys

def main():
    lines = read_file(day=11)
    monkeys = parse_monkeys(lines=lines)
    
    rounds = 20
    monkeys = monkey_business(monkeys=monkeys, rounds=rounds)
    inspected = sorted([m.inspected for m in monkeys], reverse=True)
    print(f'Part 1: The level of monkey business after 20 rounds of stuff-slinging simian shenanigans is {inspected[0] * inspected[1]}')
    
    monkeys = parse_monkeys(lines=lines)
        
    rounds = 10000
    monkeys = monkey_business(monkeys=monkeys, rounds=rounds, decrease_worry=False)
    inspected = sorted([m.inspected for m in monkeys], reverse=True)
    print(f'Part 2: The level of monkey business after 10000 rounds is {inspected[0] * inspected[1]}')

if __name__ == '__main__':
    main()
