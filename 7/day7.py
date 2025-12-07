import sys

manifold = {}
starts = []

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f.read().splitlines():
        x = 0
        for c in line:
            if c == 'S':
                start = (x,y)
                c = '.'
            manifold[(x,y)] = c
            x += 1
        width = x
        y += 1
    height = y

def run_beam(manifold, visited, height, start):
    for y in range(start[1], height):
        next_pos = (start[0],y)
        if visited.get(next_pos):
            return 0
        elif manifold[next_pos] == '^':
            return 1 + run_beam(manifold, visited, height, (start[0]-1,y)) + run_beam(manifold, visited, height, (start[0]+1,y))
        else:
            visited[next_pos] = 1
    return 0


print(f"part1: {run_beam(manifold, {}, height, start)}")

def run_quantum_beam(manifold, lookup, height, start):
    for y in range(start[1], height):
        next_pos = (start[0],y)
        if manifold[next_pos] == '^':
            if next_pos not in lookup:
                lookup[next_pos] = run_quantum_beam(manifold, lookup, height, (start[0]-1,y)) + run_quantum_beam(manifold, lookup, height, (start[0]+1,y))
            return lookup[next_pos]

    return 1


print(f"part2: {run_quantum_beam(manifold, {}, height, start)}")
