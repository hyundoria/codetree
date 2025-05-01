a, b = map(int, input().split())
n = int(input())

arr = []

while n > 0:
    arr.append(n % 10)
    n = int(n / 10)

for x in range(1, len(arr)):
    arr[x] = arr[x-1] + (arr[x] * pow(a,x))

new = arr[len(arr) - 1]

subarr = []

while new > 0:
    subarr.append(new%b)
    new = int(new / b)

for k in subarr[::-1] :
    print(k, end="")

