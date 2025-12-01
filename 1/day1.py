import sys

dial = 50
zeroes_part1 = 0
zeroes_part2 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        rot = 1 if line[0] == "R" else -1
        steps = int(line[1:])
        laps = int(steps / 100)

        prev_dial = dial
        dial = (dial + (rot*steps)) % 100
        if dial == 0:
            zeroes_part1 += 1

        zeroes_part2 += laps
        if prev_dial != 0 and ((rot > 0 and prev_dial > dial) or (rot < 0 and (dial > prev_dial) or dial == 0)):
            zeroes_part2 += 1
            

print(f"part1: {zeroes_part1}")
print(f"part2: {zeroes_part2}")

