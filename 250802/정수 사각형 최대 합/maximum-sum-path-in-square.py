n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

ans = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):

        ans[i][j] = max((ans[i-1][j] + grid[i-1][j-1]), ans[i][j-1] + grid[i-1][j-1])
        
print(ans[n][n])