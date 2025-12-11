import sys

tiles = []

connections = {}
with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        node, output_str = line.split(':')
        outputs = output_str.strip().split(' ')
        connections[node] = outputs

def dfs(connections, node, goal, lookup, skip):
    if node == goal:
        return 1

    if not node in connections:
        return 0

    if node in lookup:
        return lookup[node]

    num_paths = 0
    for output in connections[node]:
        if output in skip:
            continue

        num_new_paths = dfs(connections, output, goal, lookup, skip)
        lookup[output] = num_new_paths
        num_paths += num_new_paths

    return num_paths

print(f"part1: {dfs(connections, 'you', 'out', dict(), set())}")

num_paths  = dfs(connections, 'svr', 'fft', dict(), {'dac','out'}) * dfs(connections, 'fft', 'dac', dict(), {'svr','out'}) * dfs(connections, 'dac', 'out', dict(), {'fft','svr'}) + dfs(connections, 'svr', 'dac', dict(), {'fft', 'out'}) * dfs(connections, 'dac', 'fft', dict(), {'svr', 'out'}) *  dfs(connections, 'fft', 'out', dict(), {'svr','dac'})
print(f"part2: {num_paths}")




#print(len(dfs(connections, 'svr', 'out', set(), {}, {'fft','dac'})))
#print(len(dfs(connections, 'svr', list(), 'out')))
