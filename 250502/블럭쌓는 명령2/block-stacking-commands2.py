n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = []

for i in range(n+1):
    arr.append(0)

for k in commands:
    for i in range(k[0],k[1]+1):
        arr[i] += 1

print(max(arr))