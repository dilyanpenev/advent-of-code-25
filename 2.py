def solve_task_1():
    with open('inputs/2.txt', 'r') as f:
        ranges = [rng.strip() for rng in f.readlines()[0].strip().split(',')]
    result = 0
    for rng in ranges:
        start, end = map(int, rng.split('-'))
        while len(str(start))%2 != 0 and start <= end:
            start += 1
        length = len(str(start))
        while start <= end:
            half_length = length // 2
            first_half = str(start)[:half_length]
            second_half = str(start)[half_length:]
            if first_half == second_half:
                result += start
                # print("Found fake ID:", start)
            start += 1

    print("The result for task 1 is: ", result)


def solve_task_2():
    with open('inputs/2.txt', 'r') as f:
        ranges = [rng.strip() for rng in f.readlines()[0].strip().split(',')]
    result = 0
    for rng in ranges:
        start, end = map(int, rng.split('-'))
        while start <= end:
            length = len(str(start))
            for sec in range(1, length//2 + 1):
                first_sec = str(start)[:sec]
                for i in range(sec, length, sec):
                    if str(start)[i:i+sec] != first_sec:
                        break
                else:
                    result += start
                    print("Found fake ID:", start)
                    break
            start += 1

    print("The result for task 2 is: ", result)

if __name__ == "__main__":
    solve_task_1()
    solve_task_2()