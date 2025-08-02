n = int(input())

pivo = [0, 1, 1]

for i in range(3, n+1):
    pivo.append(pivo[i-2] + pivo[i-1])

print(pivo[n])