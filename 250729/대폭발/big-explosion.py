n, m, r, c = map(int, input().split())

arr = [[0] * n for _ in range(n)]

arr[r-1][c-1] = 1

dxy = [[-1,0],[1,0],[0,1],[0,-1]]


for d in range(1, m+1):

    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n): 
            if arr[i][j] == 1:

                new_arr[i][j] = 1

                for dx, dy in dxy:

                    nx = i + (dx*d)
                    ny = j + (dy*d)

                    if 0 <= nx < n and 0 <= ny < n:
                        new_arr[nx][ny] = 1

    arr = new_arr

cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)