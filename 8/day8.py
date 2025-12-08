import sys

boxes = []
with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        x, y, z = [int(val) for val in line.split(',')]
        boxes.append((x,y,z))

distances = {}
for i in range(0, len(boxes)):
    for j in range(i+1, len(boxes)):
        box_a = boxes[i]
        box_b = boxes[j]
        dist = ((box_a[0]-box_b[0])**2 + (box_a[1]-box_b[1])**2 + (box_a[2]-box_b[2])**2)**0.5
        if dist not in distances:
            distances[dist] = set()
        distances[dist].add((i,j))


def do_connect(connected, i, new_connections):
    for remote in connected[i]:
        connected[remote] |= new_connections

    connected[i] |= new_connections

def connect_boxes(distances, connection_limit, num_boxes):
    connected = dict()
    num_connected = 0
    last_connection = None
    for distance in sorted(distances):
        for i,j in distances[distance]:
            num_connected += 1
            if connected.get(i) and j in connected[i]:
                continue

            if not i in connected:
                connected[i] = set()
            if not j in connected:
                connected[j] = set()

            connect_to_i = connected[j] | set([j])
            connect_to_j = connected[i] | set([i])
            do_connect(connected, i, connect_to_i)
            do_connect(connected, j, connect_to_j)

        if num_connected == connection_limit or len(connected[i]) == num_boxes - 1:
            last_connection = (i,j)
            break

    return connected, last_connection

connected, last_connection = connect_boxes(distances, 1000, len(boxes))

done = set()
total = 1
counted = 0
for key in reversed(sorted(connected, key=lambda key : len(connected[key]))):
    if key in done:
        continue
    done.add(key)
    done |= connected[key]
    total *= (len(connected[key]) + 1)
    counted += 1
    if counted >= 3:
        break

print(f"part1: {total}")
connected, last_connection = connect_boxes(distances, None, len(boxes))
print(f"part2: {boxes[last_connection[0]][0]*boxes[last_connection[1]][0]}")

