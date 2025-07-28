arr = [list(map(int, input().split())) for _ in range(4)]

direction = input()

def rotate_90(grid):

    new_grid = [[0] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            new_grid[j][3-i] = grid[i][j]

    return new_grid

if direction == 'R':
    arr = rotate_90(arr)
elif direction == 'U':
    for _ in range(2):
        arr = rotate_90(arr)
elif direction == 'L':
    for _ in range(3):
        arr = rotate_90(arr)

new_arr = []

for i in range(4):

    temp = []

    for j in range(3,-1,-1):

        if arr[j][i] != 0:
            temp.append(arr[j][i])

    new_temp = []

    flag = False

    for r in range(len(temp)):

        if flag:
            flag = False
            continue

        if r < len(temp)-1 and temp[r] == temp[r+1]:
            new_temp.append(temp[r] * 2)
            r += 1
            flag = True
        else:
            new_temp.append(temp[r])

    new_arr.append(new_temp)

arr = new_arr

for row in arr:
    for _ in range(4 - len(row)):
        row.append(0)

if direction == 'R':
    for _ in range(2):
        arr = rotate_90(arr)
elif direction == 'U':
        arr = rotate_90(arr)
elif direction == 'D':
    for _ in range(3):
        arr = rotate_90(arr)

for row in arr:
    for r in row:
        print(r, end=" ")
    print()
