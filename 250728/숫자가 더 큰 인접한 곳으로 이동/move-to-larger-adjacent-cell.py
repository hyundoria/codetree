n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

ans = [a[r][c]]


def big(x,y):

    move = [[-1,0],[1,0],[0,-1],[0,1]]

    while True:

        ch = False

        for dx, dy in move:

            nx = x+dx
            ny = y+dy

            if 1 <= nx <= n and 1 <= ny <= n:

                if a[nx][ny] > a[x][y]:
                    ans.append(a[nx][ny])
                    x, y = nx, ny
                    ch = True
                    break

        if not ch:
            break



big(r,c)

for i in ans:
    print(i, end=" ")