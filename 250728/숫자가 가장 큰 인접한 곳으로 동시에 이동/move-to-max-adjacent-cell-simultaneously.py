n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = []

for _ in range(m):

    x,y = map(int, input().split())
    x -= 1
    y -= 1
    marbles.append((x,y))


def big():

    move = [[-1,0],[1,0],[0,-1],[0,1]]

    for _ in range(t):

        cnt = [[0] * n for _ in range(n)]
        new_marbles = []

        for marble in marbles:

            r,c = marble

            max_val = a[r][c]
            mx, my = r,c

            for dx, dy in move:

                nx = r+dx
                ny = c+dy

                if 0 <= nx < n and 0 <= ny < n:

                    if a[nx][ny] > max_val:
                        max_val = a[nx][ny]
                        mx, my = nx, ny

            new_marbles.append((mx,my))
            cnt[mx][my] += 1

        marbles.clear()

        for mar in new_marbles:
            x,y = mar
            if cnt[x][y] == 1:
                marbles.append((x,y))

    print(len(marbles))

big()

