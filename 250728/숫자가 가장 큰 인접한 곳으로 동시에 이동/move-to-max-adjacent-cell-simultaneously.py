n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    cnt[x-1][y-1] = 1

dxy = [(-1,0), (1,0), (0,-1), (0,1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y) -> tuple[int, int]:
    ans_max = 0
    ans_x, ans_y = -1, -1

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and a[nx][ny] > ans_max:
            ans_max = a[nx][ny]
            ans_x, ans_y = nx, ny

    return ans_x, ans_y

for _ in range(t):

    next_cnt = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if  cnt[i][j] > 0:
                nx, ny = move(i,j)
                next_cnt[nx][ny] += 1

    for i in range(n):
        for j in range(n):
            cnt[i][j] = next_cnt[i][j]
            if cnt[i][j] >= 2:
                cnt[i][j] = 0

ans  = 0

for i in range(n):
    for j in range(n):
        ans += cnt[i][j]

print(ans)