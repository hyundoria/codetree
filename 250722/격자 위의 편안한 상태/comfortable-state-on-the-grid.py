n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

move = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(m):

    r, c = map(int, input().split())
    r ,c = r-1, c-1
    arr[r][c] = 1

    cnt = 0

    for dx, dy in move:
        nx = r + dx
        ny = c + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if arr[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)