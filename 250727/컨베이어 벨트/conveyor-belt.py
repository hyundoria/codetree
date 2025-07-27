n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = u + d

for _ in range(t):

    temp = arr[2*n-1]

    for i in range(2*n-1, 0, -1):
        
        arr[i] = arr[i-1]

    arr[0] = temp

for i in range(len(arr)):
    print(arr[i], end=" ")
    if (i+1) % n == 0:
        print()
