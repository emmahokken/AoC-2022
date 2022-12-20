import re
from utils.read_file import read_file, read_test_file

class Supplies():
    def __init__(self):
        self.ore_robot = 1
        self.clay_robot = 0
        self.obsidian_robot = 0
        self.geode_robot = 0
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0

    def add_ore(self):
        self.ore += 1

    def add_clay(self):
        self.clay += 1

    def add_obsidian(self):
        self.obsidian += 1

    def add_geode(self):
        self.geode += 1

    def add_ore_robit(self, cost):
        self.ore_robot += 1
        self.ore -= cost

    def add_clay_robit(self, cost):
        self.clay_robot += 1
        self.ore -= cost

    def add_obsidian_robit(self, ore_cost, clay_cost):
        self.obsidian_robot += 1
        self.ore -= ore_cost
        self.clay -= clay_cost

    def add_geode_robit(self, ore_cost, obsidian_cost):
        self.geode_robot += 1
        self.ore -= ore_cost
        self.obsidian -= obsidian_cost

    def __repr__(self):
        return f'You have {self.ore} ore, {self.clay} clay, {self.obsidian} obsidian, and {self.geode} geode'

class Blueprint():

    def __init__(self, name, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
        self.name = name
        self.ore_cost = ore
        self.clay_cost = clay
        self.obsidian_ore_cost = obsidian_ore
        self.obsidian_clay_cost = obsidian_clay
        self.geode_ore_cost = geode_ore
        self.geode_obsidian_cost = geode_obsidian

    def __repr__(self):
        return f'Blueprint: Each ore robot costs {self.ore_cost} ore. Each clay robot costs {self.clay_cost} ore. Each \
        obsidian robot costs {self.obsidian_ore_cost} ore and {self.obsidian_clay_cost} clay. Each geode robot costs \
        {self.geode_ore_cost} ore and {self.geode_obsidian_cost} obsidian.'

def main():

    lines = read_test_file(day=19)
    blueprints = []
    for line in lines:
        name, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = re.findall(r'\d+', line)
        b = Blueprint(int(name), int(ore), int(clay), int(obsidian_ore), int(obsidian_clay), int(geode_ore), int(geode_obsidian))
        blueprints.append(b)

    quality = []
    for blue in blueprints:
        sup = Supplies()
        for minute in range(24):
            print(f'\n\nMinute: {minute + 1}')

            for _ in range(sup.ore_robot):
                sup.add_ore()
                print(f'add ore')
            for _ in range(sup.clay_robot):
                sup.add_clay()
                print(f'add clay')
            for _ in range(sup.obsidian_robot):
                sup.add_obsidian()
                print(f'add obsidian')
            for _ in range(sup.geode_robot):
                sup.add_geode()
                print(f'add geode')

            print(sup)

            if sup.ore > blue.geode_ore_cost and sup.obsidian > blue.geode_obsidian_cost:
                sup.add_geode_robit(blue.geode_ore_cost, blue.geode_obsidian_cost)
                print(f'add geode robit, you now have {sup.geode_robot}')
            elif sup.ore > blue.obsidian_ore_cost and sup.clay > blue.obsidian_clay_cost:
                sup.add_obsidian_robit(blue.obsidian_ore_cost, blue.obsidian_clay_cost)
                print(f'add obsidian robit, you now have {sup.obsidian_robot}')
            elif sup.ore > blue.clay_cost:
                sup.add_clay_robit(blue.clay_cost)
                print(f'add clay robit, you now have {sup.clay_robot}')
            elif sup.ore > blue.ore_cost:
                sup.add_ore_robit(blue.ore_cost)
                print(f'add clay robit, you now have {sup.clay_robot}')

            print(sup)
        print(sup)
        print('\n\n')
        quality.append(blue.name*sup.geode)
        exit()

    print(sum(quality))

if __name__ == '__main__':
    main()