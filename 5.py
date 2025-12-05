def solve_task_1():
    with open('inputs/5.txt', 'r') as f:
        line = f.readline().strip()
        ranges, items = [], []
        while line != '':
            l, r = map(int, line.split('-'))
            ranges.append((l, r))
            line = f.readline().strip()
        
        # reached empty line
        line = f.readline().strip()
        while line != '':
            items.append(int(line))
            line = f.readline().strip()

    result = 0
    for item in items:
        for rng in ranges:
            if item >= rng[0] and item <= rng[1]:
                result += 1
                # print("Fresh ID: ", item)
                break

    print("The result for task 1 is: ", result)


def solve_task_2():
    with open('inputs/5.txt', 'r') as f:
        line = f.readline().strip()
        ranges, items = [], []
        while line != '':
            l, r = map(int, line.split('-'))
            ranges.append((l, r))
            line = f.readline().strip()
        # reached empty line

    result = 0
    tested = []
    for left, right in ranges:
        for i, (tleft, tright) in enumerate(tested):
            if tleft <= left and left <= tright:
                if right > tright:
                    tested[i][1] = right
                break
            if tleft <= right and right <= tright:
                if left < tleft:
                    tested[i][0] = left
                break
        else:
            tested.append([left,right])
    for i in range(len(tested)):
        for j in range(len(tested)):
            if i != j:
                if tested[j][0] <= tested[i][0] and tested[i][0] <= tested[j][1]:
                    tested[i][0] = tested[j][1] + 1
                if tested[j][0] <= tested[i][1] and tested[i][1] <= tested[j][1]:
                    tested[i][1] = tested[j][0] - 1
    for left, right in tested:
        if right >= left:
            result += right - left + 1

    print("The result for task 2 is: ", result)


if __name__ == "__main__":
    solve_task_1()
    solve_task_2()