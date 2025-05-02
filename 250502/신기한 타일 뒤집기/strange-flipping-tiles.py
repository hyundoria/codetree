n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)



arr = [0 for i in range(200_001)]

location = 0
ran = 0

for i in range(n):

    if dir[i] == "R":

        ran = location + x[i]
        for j in range(location+100_000, ran+100_000):
            arr[j] = 2
        location = ran - 1

    else:
        location += 1
        ran = location - x[i]
        for j in range(ran+100_000, location+100_000):
            arr[j] = 1
        location = ran

color = [0 for i in range(2)]

for i in range(200_001):
    if arr[i] == 1:
        color[0] += 1
    elif arr[i] == 2:
        color[1] += 1


print(f'{color[0]} {color[1]}')
