n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def check(x,y):

    move = [[0,1],[1,0],[0,-1],[-1,0]]

    cnt = 0

    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            cnt += 1

    return cnt


cnt = 0

for i in range(n):
    for j in range(n):
        if check(i,j) >= 3:
            cnt += 1




print(cnt)

