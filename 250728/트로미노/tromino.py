n,m = map(int, input().split())

arr =[list(map(int, input().split())) for _ in range(n)]

dxy = [[0,0],[1,0],[0,1],[1,1]]

val = 0

for i in range(n-1):
    for j in range(m-1):

        q = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]

        for dx, dy in dxy:

            sub = q - arr[i + dx][j + dy]

            val = max(sub, val)

        if  j < m-2:

            q = arr[i][j] + arr[i][j+1] + arr[i][j+2]

            val = max(q, val)

        if i < n-2:

            q = arr[i][j] + arr[i+1][j] + arr[i+2][j]

            val = max(q, val)

for i in range(m-2):

    q = arr[n-1][i] + arr[n-1][i+1] + arr[n-1][i+2]

    val = max(q, val)

for i in range(n-2):

    q = q = arr[i][m-1] + arr[i+1][m-1] + arr[i+2][m-1]

    val = max(q, val)

print(val)