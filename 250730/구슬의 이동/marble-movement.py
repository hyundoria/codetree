n,m,t,k = map(int, input().split())

marbles = []

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

diretion = {

    'U' : 0,
    'R' : 1,
    'D' : 2,
    'L' : 3
}

for i in range(m):

    r,c,d,v = input().split()

    r,c,v = int(r), int(c), int(v)
    r -= 1
    c -= 1
    d = diretion[d]
    marbles.append([r,c,d,v,i+1])

for _ in range(t):
    
    new_marble = []
    arr = [[[] for _ in range(n)] for _ in range(n)]

    for marble in marbles:

        r,c,d,v,i = marble[0],marble[1],marble[2],marble[3],marble[4],

        for _ in range(v):

            nx = r + dxy[d][0]
            ny = c + dxy[d][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                d = (d+2) % 4
                nx = r + dxy[d][0]
                ny = c + dxy[d][1]
            r,c = nx, ny
        
        arr[r][c].append([r,c,d,v,i])
    
    for i in range(n):
        for j in range(n):

            if len(arr[i][j]) > k:
                arr[i][j].sort(key=lambda x: (-x[3], -x[4]))

                for _ in range(len(arr[i][j]) - k):
                    arr[i][j].pop()

            for marble in arr[i][j]:
                new_marble.append(marble)
    
    
    marbles = new_marble

print(len(marbles))
