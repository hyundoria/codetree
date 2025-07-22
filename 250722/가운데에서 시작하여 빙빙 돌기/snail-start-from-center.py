n = int(input())

arr = [[0] * n for _ in range(n)]

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

direction = 3

num = n*n

x, y = n-1, n-1

while num != 0:

    arr[x][y] = num
    num -= 1

    nx = x + move[direction][0]
    ny = y + move[direction][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = x + move[direction][0]
        ny = y + move[direction][1]

    x, y = nx, ny

for row in arr:
    for i in row:
        print(i, end=" ")
    print()



