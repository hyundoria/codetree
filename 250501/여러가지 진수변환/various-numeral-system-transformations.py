N, B = map(int, input().split())

if N == 0:
    print(0)
    exit(0)

arr = []

if B == 4:
    while N > 0:
        arr.append(N % 4)
        N = int(N / 4)
elif B == 8:
    while N > 0:
        arr.append(N % 8)
        N = int(N / 8)



for k in arr[::-1] :
    print(k, end="")

