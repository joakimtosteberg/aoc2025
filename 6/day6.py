import sys

problems = []
operations = []
problem_lines = []
operation_line = ""

with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        inputs = line.split()
        if inputs[0] == '*' or inputs[0] == '+':
            operations = inputs
            operation_line = line
            continue
        problem_lines.append(line)
        if not problems:
            for i in range(0,len(inputs)):
                problems.append([])
        for i in range(0,len(inputs)):
            problems[i].append(int(inputs[i]))


def solve_problems(problems, operations):
    total = 0
    for i in range(0,len(problems)):
        if operations[i] == '+': 
            op = lambda a,b: a + b
            solution = 0
        else:
            op = lambda a,b: a * b
            solution = 1
        for value in problems[i]:
            solution = op(solution, value)
        total += solution

    return total

print(f"part1: {solve_problems(problems, operations)}")

next_op = None
next_solution = None
fixed_problems = []
start = 0
total = 0
last = False
for i in range(0,len(operation_line)):
    if operation_line[i] == '+':
        op = next_op
        solution = next_solution
        next_op = lambda a,b: a + b
        next_solution = 0
    elif operation_line[i] == '*':
        op = next_op
        solution = next_solution
        next_op = lambda a,b: a * b
        next_solution = 1
    elif i == len(operation_line) - 1:
        op = next_op
        solution = next_solution
        i += 2
        last = True
    else:
        continue

    if not op:
        continue

    end = i - 1
    for pos in range(end-1, start-1, -1):
        value = ""
        for problem_line in problem_lines:
            value += problem_line[pos]
        solution = op(solution, int(value))
    total += solution
    start = i
        
    

print(f"part2: {total}")
