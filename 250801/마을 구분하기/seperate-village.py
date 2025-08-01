from collections import deque

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

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

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))
    
    count.append(cnt)

cnt = 0
count = []

for i in range(n):
    for j in range(n):

        if grid[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(i,j)


count.sort()
print(cnt)
for c in count:
    print(c)

