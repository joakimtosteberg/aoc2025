import sys

tiles = []
with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        x, y = [int(val) for val in line.split(',')]
        tiles.append((x,y))


max_area = 0
for i in range(0, len(tiles)):
    for j in range(i+1, len(tiles)):
        area = (abs(tiles[i][0]-tiles[j][0])+1)*(abs(tiles[i][1]-tiles[j][1])+1)
        max_area = max(area, max_area)

print(f"part1: {max_area}")
