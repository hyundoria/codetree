n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = []

# -100 = 0, 0 = 100, 100 = 200
for i in range(101):
    arr.append(0)

for k in segments:
    for i in range(k[0],k[1]+1):
        arr[i] += 1

print(max(arr))