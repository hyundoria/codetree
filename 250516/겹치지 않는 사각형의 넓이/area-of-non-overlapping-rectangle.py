x1, y1, x2, y2 = [], [], [], []

arr = [[0] * 2001 for i in range(2001)]

for _ in range(3):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

    if _ == 2:
        for j in range(x1[_], x2[_]):
            for r in range(y1[_], y2[_]):
                arr[j][r] = 0
    else:
        for j in range(x1[_], x2[_]):
            for r in range(y1[_], y2[_]):
                arr[j][r] = 1

print(sum([row.count(1) for row in arr]))
