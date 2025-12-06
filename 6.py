import math

def solve_task_1():
    with open('inputs/6.txt', 'r') as f:
        lines = [line.strip() for line in f]
    nums, signs = [], []
    for idx, line in enumerate(lines):
        if idx == len(lines)-1:
            signs = line.split()
        else:
            nums.append(list(map(int, line.split())))

    result = 0
    for idx, sign in enumerate(signs):
        if sign == '+':
            result += sum([x[idx] for x in nums])
        elif sign == '*':
            result += math.prod([x[idx] for x in nums])
    print("The result for task 1 is: ", result)


def solve_task_2():
    with open('inputs/6.txt', 'r') as f:
        lines = [line[:-1] for line in f]
    nums, signs = [], []
    signs = lines[-1].split()
    
    ns = []
    for i in range(max([len(line) for line in lines[:-1]])):
        n = ''
        for line in lines[:-1]:
            n += line[i]
        n = n.strip()
        if n == "":
            nums.append(ns)
            ns = []
        else:
            ns.append(int(n))
    nums.append(ns)

    result = 0
    for idx, sign in enumerate(signs):
        if sign == '+':
            result += sum(nums[idx])
        elif sign == '*':
            result += math.prod(nums[idx])
    print("The result for task 2 is: ", result)


if __name__ == "__main__":
    solve_task_1()
    solve_task_2()