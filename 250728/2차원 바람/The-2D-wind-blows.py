import copy

n,m,q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dxy = [[0,-1],[1,0],[0,1],[-1,0]]


for _ in range(q):

    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    x, y = r1, c1
    temp = arr[x][y]
    num = 1

    while True:

        nx = x + dxy[num][0]
        ny = y + dxy[num][1]

        if nx == r1 and ny == c1:
            arr[x][y] = temp
            break

        if r1 <= nx <= r2 and c1 <= ny <= c2:
            arr[x][y] = arr[nx][ny]
            x,y = nx,ny
        else:
            num = (num+1)%4
            continue


    new_arr = copy.deepcopy(arr)


    for i in range(r1, r2+1):
        for j in range(c1, c2+1):

            val = arr[i][j]
            cnt = 1

            for dx, dy in dxy:

                nx = i + dx
                ny = j + dy

                if 0 <= nx < n and 0 <= ny < m:
                    val += arr[nx][ny]
                    cnt += 1

            new_arr[i][j] = int(val / cnt)

    arr = copy.deepcopy(new_arr)

for row in arr:
    for k in row:
        print(k, end=" ")
    print()