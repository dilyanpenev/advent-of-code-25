def solve_task_1():
    with open('inputs/3.txt', 'r') as f:
        banks = [line.strip() for line in f]
    
    result = 0
    for bank in banks:
        batteries = [int(c) for c in bank]
        max_first = max(batteries[:len(batteries)-1])
        max_index = batteries.index(max_first)
        max_second = max(batteries[max_index+1:])
        # print("Max joltage: ", max_first*10+max_second)
        result += max_first*10+max_second
    
    print("The result for task 1 is: ", result)

def solve_task_2():
    with open('inputs/3.txt', 'r') as f:
        banks = [line.strip() for line in f]
    
    result = 0
    for bank in banks:
        batteries = [int(c) for c in bank]
        jolt = 0
        for i in range(11, -1, -1):
            max_first = max(batteries[:len(batteries)-i])
            max_index = batteries.index(max_first)
            jolt += max_first * (10 ** i)
            batteries = batteries[max_index+1:]
        print("Max joltage: ", jolt)
        result += jolt

    print("The result for task 2 is: ", result)

if __name__ == "__main__":
    solve_task_1()
    solve_task_2()