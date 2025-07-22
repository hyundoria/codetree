n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

move = [[0,1],[1,0],[0,-1],[-1,0]]

num = 0

if d == 'R':
    num = 1
elif d == 'D':
    num = 2
elif d == 'L':
    num = 3

for _ in range(t):

    nx = r + move[num][1]
    ny = c + move[num][0]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        num = (num + 2) % 4
        continue
    
    r,c = nx, ny

print(r,c)