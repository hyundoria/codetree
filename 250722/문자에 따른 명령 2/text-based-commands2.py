moves = input()

x,y = 0, 0

move = [[0,1],[1,0],[0,-1],[-1,0]]

num = 0

for direction in moves:

    if direction == 'R':
        num = (num + 1) % 4
    elif direction == 'L':
        num = (num - 1) % 4
    else:
        x, y = x + move[num][0], y + move[num][1]

print(x,y)
