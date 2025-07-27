n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
m = 0

for i in range(n-2):
    for j in range(n-2):
        for k in range(3):
            for r in range(3):
                if grid[i+k][r+j] == 1:
                    cnt += 1
        m = max(cnt, m)
        cnt = 0

print(m)