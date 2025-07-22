n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

move = [[-1,0],[0,1],[1,0],[0,-1]]

direction = 1

num = 1

x,y = 0,0

while num != ((n*m)+1):
    
    arr[x][y] = num
    num += 1

    nx = x + move[direction][0]
    ny = y + move[direction][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = x + move[direction][0]
        ny = y + move[direction][1]
    
    x,y = nx, ny


for row in arr:
    for i in row:
        print(i, end=" ")
    print()



