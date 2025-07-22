n = int(input())

x,y = 0, 0

move = [[0,1],[1,0],[0,-1],[-1,0]]

for _ in range(n):

    direction, length = input().split()

    length = int(length)

    num = 0

    if direction == 'N':
        num = 0
    elif direction == 'S':
        num = 2
    elif direction == 'E':
        num = 1
    elif direction == 'W':
        num = 3

    x, y = x + (move[num][0] * length), y + (move[num][1] * length)

print(x,y)
