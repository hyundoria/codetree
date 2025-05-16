arr = [[0] * 201 for i in range(201)]

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

for i in range(n):
    for j in range(x[i], x[i] + 8):
        for r in range(y[i], y[i] + 8):
                arr[j][r] = 1

print(sum([row.count(1) for row in arr]))
