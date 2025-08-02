from collections import deque

n, h, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dxy = [[-1,0],[0,-1], [1,0],[0,1]]

def bfs(x,y):

    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x,y = q.popleft()

        for dx,dy in dxy:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                if grid[nx][ny] == 3:
                    return visited[nx][ny]
                q.append((nx,ny))

    return -1

ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            ans[i][j] = bfs(i,j)
    

for row in ans:
    for r in row:
        print(r, end=" ")
    print()