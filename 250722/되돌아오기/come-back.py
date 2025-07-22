n = int(input())

direction = {
    'N':(0,1),
    'E':(1,0),
    'S':(0,-1),
    'W':(-1,0)
}

x, y = 0, 0

sec = 0

for _ in range(n):

    d, l = input().split()
    l = int(l)

    for _ in range(l):

        dx = x + direction[d][0]
        dy = y + direction[d][1]
        sec += 1

        if dx == 0 and dy == 0:
            print(sec)
            exit(0)
        x, y = dx, dy

print(-1)