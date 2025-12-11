import sys

tiles = []

connections = {}
with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        node, output_str = line.split(':')
        outputs = output_str.strip().split(' ')
        connections[node] = outputs

def dfs(connections, node, path, goal):
    if node == goal:
        return [path]

    if not node in connections:
        return []

    paths = []
    for output in connections[node]:
        paths += dfs(connections, output, path + [node], goal)

    return paths

print(len(dfs(connections, 'you', list(), 'out')))

