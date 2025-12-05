import sys

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        print(f"{self.start}:{self.end}")

    def __repr__(self):
        return f"{self.start}:{self.end}"

ranges = []
ids = []

def merge_ranges(range_a, range_b):
    if range_b.start > range_a.end or range_b.end < range_a.start:
        return None

    return Range(min(range_a.start, range_b.start), max(range_a.end, range_b.end))

def merge_into_ranges(ranges, id_range):
    new_ranges = []
    for check_range in ranges:
        merged_range = merge_ranges(check_range, id_range)
        if merged_range:
            id_range = merged_range
        else:
            new_ranges.append(check_range)
    new_ranges.append(id_range)
    return new_ranges

    

with open(sys.argv[1], "r") as f:
    parse_ranges = True
    for line in f.read().splitlines():
        if parse_ranges:
            if not line:
                parse_ranges = False
                continue
            start, end = line.split('-')
            ranges = merge_into_ranges(ranges, Range(int(start), int(end)))
        else:
            ids.append(int(line))

fresh = 0
for id in ids:
    for range in ranges:
        if id >= range.start and id <= range.end:
            fresh += 1
            break

print(f"part1: {fresh}")
total_fresh = 0
for id_range in ranges:
    total_fresh += id_range.end - id_range.start + 1

print(f"part2: {total_fresh}")
