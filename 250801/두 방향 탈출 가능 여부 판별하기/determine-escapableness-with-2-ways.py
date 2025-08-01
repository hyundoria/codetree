from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dxy = [[1,0],[0,1]]

def bfs(x,y):

    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for dx,dy in dxy:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))

bfs(0,0)

if not visited[n-1][m-1]:
    print(0)
else:
    print(1)



