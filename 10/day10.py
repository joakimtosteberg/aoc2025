import sys

class Machine:
    def __init__(self, indicators, joltage_req, buttons):
        self.wanted_indicators = indicators
        self.joltage_req = joltage_req
        self.buttons = buttons

    def run(self):
        lookup = dict()
        lookup[0] = 0

        presses = 0
        states = []
        next_states = [0]
        while next_states:
            states = next_states
            next_states = []
            presses += 1
            for state in states:
                for button in self.buttons:
                    next_indicators = state ^ button
                    if next_indicators in lookup:
                        continue

                    if next_indicators == self.wanted_indicators:
                        return presses

                    lookup[next_indicators] = presses
                    next_states.append(next_indicators)

        return presses

machines = list()

with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        data = line.split(' ')
        indicators_str = data[0].strip("[]")
        indicators = 0
        for i in range(0,len(indicators_str)):
            if indicators_str[i] == '#':
                indicators += 2**i
        joltage_req = [int(val) for val in(data[-1].strip("{}").split(","))]
        buttons = list()
        for i in range(1, len(data)-1):
            button = 0
            for indicator in data[i].strip("()").split(","):
                button |= 2**int(indicator)
            buttons.append(button)
        machines.append(Machine(indicators, joltage_req, buttons))

total = 0
for machine in machines:
    total += machine.run()

print(f"part1: {total}")
