from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

start = [list(map(int, input().split())) for _ in range(k)]

dxy = [[-1,0],[0,-1], [1,0],[0,1]]

def bfs(x,y):

    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for dx,dy in dxy:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))

    return cnt


cnt = 0

for i,j in start:
    if not visited[i-1][j-1]:
        cnt += bfs(i-1,j-1)

print(cnt)