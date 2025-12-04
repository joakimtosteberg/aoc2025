import sys

steps = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

adjacency = {}
with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in line.strip():
            pos = (x,y)
            if c == '@':
                adjacency[pos] = 0
                for step in steps:
                    next_pos = (pos[0]+step[0],pos[1]+step[1])
                    if next_pos in adjacency:
                        adjacency[next_pos] += 1
                        adjacency[pos] += 1
            x += 1
        y += 1

print(f"part1: {len([x for x in adjacency.values() if x < 4])}")

removed = 0
did_remove = False
while True:
    did_remove = False
    for pos in list(adjacency):
        if adjacency[pos] < 4:
            del adjacency[pos]
            did_remove = True
            removed += 1
            for step in steps:
                next_pos = (pos[0]+step[0],pos[1]+step[1])
                if next_pos in adjacency:
                    adjacency[next_pos] -= 1

    if not did_remove:
        break

print(f"part2: {removed}")
