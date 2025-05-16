n = int(input())
x1, y1, x2, y2 = [], [], [], []

arr = [[0] * 201 for i in range(201)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

    for j in range(x1[_], x2[_]):
        for r in range(y1[_], y2[_]):
            arr[j][r] = 1

print(sum([row.count(1) for row in arr]))
