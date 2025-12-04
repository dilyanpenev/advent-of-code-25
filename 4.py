def solve_task_1():
    with open('inputs/4.txt', 'r') as f:
        lines = [line.strip() for line in f]

    result = 0
    length = len(lines[0])
    for line_num in range(len(lines)):
        for i in range(length):
            if lines[line_num][i] != '@':
                continue
            cnt = 0
            for j in range(-1, 2):
                if line_num+j >= 0 and line_num+j < length:
                    if i > 0 and lines[line_num+j][i-1] == '@':
                        cnt += 1
                    if lines[line_num+j][i] == '@':
                        cnt += 1
                    if i < length-1 and lines[line_num+j][i+1] == '@':
                        cnt += 1
            if cnt < 5:
                # print("Found paper roll at row ", line_num, " column ", i, " with cnt=", cnt)
                result += 1

    print("The result for task 1 is: ", result)


def solve_task_2():
    with open('inputs/4.txt', 'r') as f:
        grid = [list(line.strip()) for line in f]

    result, loop_result = 0, 1
    length = len(grid[0])
    while loop_result > 0:
        loop_result = 0
        taken = []
        for line_num in range(len(grid)):
            for i in range(length):
                if grid[line_num][i] != '@':
                    continue
                cnt = 0
                for j in range(-1, 2):
                    if line_num+j >= 0 and line_num+j < length:
                        if i > 0 and grid[line_num+j][i-1] == '@':
                            cnt += 1
                        if grid[line_num+j][i] == '@':
                            cnt += 1
                        if i < length-1 and grid[line_num+j][i+1] == '@':
                            cnt += 1
                if cnt < 5:
                    loop_result += 1
                    taken.append((line_num, i))
        # print("The rolls taken this loop: ", loop_result)
        result += loop_result
        for coord in taken:
            grid[coord[0]][coord[1]] = 'x'

    print("The result for task 2 is: ", result)


if __name__ == "__main__":
    solve_task_1()
    solve_task_2()