def solve_task_1():
    with open('inputs/1.txt', 'r') as f:
        lines = [line.strip() for line in f]
    
    direction, length = '', 0
    current_position = 50
    result = 0
    for line in lines:
        direction = line[0]
        length = int(line[1:])
        if direction == 'R':
            current_position += length
        elif direction == 'L':
            current_position -= length
        current_position = abs(current_position%100)
        if current_position == 0:
            result += 1
    
    print("The result for task 1 is: ", result)

def solve_task_2():
    with open('inputs/1.txt', 'r') as f:
        lines = [line.strip() for line in f]
    
    direction, length = '', 0
    current_position = 50
    result = 0
    for line in lines:
        direction = line[0]
        length = int(line[1:])
        if direction == 'R':
            current_position += length
        elif direction == 'L':
            current_position -= length
        result += abs(current_position//100)
        if current_position < 0 and abs(current_position)%100 == 0:
            result += 1
        if current_position == 0:
            result += 1
        if abs(current_position) == length and current_position < 0:
            result -= 1
        current_position = abs(current_position%100)

    print("The result for task 2 is: ", result)

if __name__ == "__main__":
    solve_task_1()
    solve_task_2()