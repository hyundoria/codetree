n = int(input())
x = []
dir = []

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)


arr = [0 for i in range(2001)]

location = 0
ran = 0

for i in range(n):
    if dir[i] == "R":
        ran = location + x[i]
        for j in range(location, ran):
            arr[j+1000] += 1
    else:
        ran = location - x[i]
        for j in range(ran, location):
            arr[j+1000] += 1
    location = ran

ran = 0

for i in arr:
    if i > 1:
        ran += 1

print(ran)
