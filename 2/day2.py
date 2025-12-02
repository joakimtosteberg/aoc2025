import sys

def is_invalid_seq_len(num, seq_len):
    for i in range(1, int(len(num)/ seq_len)):
        if num[seq_len*i:seq_len*(i+1)] != num[0:seq_len]:
            return False
    return True

def is_invalid2(num):
    str_num = str(num)
    for i in range(1,int(len(str_num)/2)+1):
        if len(str_num) % i == 0 and is_invalid_seq_len(str_num, i):
            return True
    return False

def is_invalid1(num):
    str_num = str(num)
    if len(str_num) % 2 == 1:
        return False
    return is_invalid_seq_len(str_num, int(len(str_num) / 2))

invalid1_sum = 0
invalid2_sum = 0
with open(sys.argv[1], "r") as f:
    for id_range in f.read().strip().split(','):
        start, end = [int(id) for id in id_range.split("-")]
        for num in range(start, end + 1):
            if is_invalid1(num):
                invalid1_sum += num
            if is_invalid2(num):
                invalid2_sum += num


print(f"Part1: {invalid1_sum}")
print(f"Part2: {invalid2_sum}")
