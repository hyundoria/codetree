from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]

dxy = [[-1,0],[0,-1], [1,0],[0,1]]

def bfs(x,y):

    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x,y = q.popleft()

        for dx,dy in dxy:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and grid[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

bfs(0,0)

print(visited[n-1][m-1])




