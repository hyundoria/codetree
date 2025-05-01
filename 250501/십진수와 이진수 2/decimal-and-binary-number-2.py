binary = int(input())

if binary == 0:
    print(0)
    exit(0)

arr = []

while binary > 0:
    arr.append(binary % 10)
    binary = int(binary / 10)

for x in range(1, len(arr)):
    arr[x] = arr[x-1] + (arr[x] * pow(2,x))

new = arr[len(arr) - 1] * 17

if new == 0:
    print(0)
    exit(0)

bin = []

while new > 0:
    bin.append(new%2)
    new = int(new / 2)

for k in bin[::-1] :
    print(k, end="")

