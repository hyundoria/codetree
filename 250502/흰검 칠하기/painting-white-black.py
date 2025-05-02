n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# row 0 : 현재 색 , 1 : 흰색 횟수, 2 : 검은색 횟수
# 흰색 1, 검은색 2, 회색 3

arr = [[0 for i in range(200_001)] for j in range(3)]

location = 0
ran = 0

for i in range(n):

    if dir[i] == "R":

        ran = location + x[i]
        for j in range(location+100_000, ran+100_000):
            if arr[0][j] != 3:
                arr[0][j] = 2
            arr[2][j] += 1

            if arr[2][j] == arr[1][j] == 2:
                arr[0][j] = 3
        location = ran - 1

    else:
        location += 1
        ran = location - x[i]
        for j in range(ran+100_000, location+100_000):
            if arr[0][j] != 3:
                arr[0][j] = 1
            arr[1][j] += 1

            if arr[2][j] == arr[1][j] == 2:
                arr[0][j] = 3
        location = ran

color = [0 for i in range(3)]

for i in range(200_001):
    if arr[0][i] == 1:
        color[0] += 1
    elif arr[0][i] == 2:
        color[1] += 1
    elif arr[0][i] == 3:
        color[2] += 1


print(f'{color[0]} {color[1]} {color[2]}')
