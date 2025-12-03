import sys

def get_max_jolt(jolts, num):
    max_jolt = [0]*num
    cur_pos = 0
    for i in range(0,len(jolts)):
        jolt = jolts[i]
        start_pos = max(0, i - (len(jolts)-len(max_jolt)))
        end_pos = min(max(i+1,len(max_jolt)),len(max_jolt))
        for j in range(start_pos,end_pos):
            if jolt > max_jolt[j] or j > cur_pos:
                max_jolt[j] = jolt
                cur_pos = j
                break
    return int(''.join([str(jolt) for jolt in max_jolt]))
    
total_jolts1 = 0
total_jolts2 = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        jolts = [int(c) for c in line.strip()]
        total_jolts1 += get_max_jolt(jolts, 2)
        total_jolts2 += get_max_jolt(jolts, 12)

print(f"part1: {total_jolts1}")
print(f"part2: {total_jolts2}")
