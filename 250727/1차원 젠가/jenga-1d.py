n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

temp = []

for i in range(n):

    if s1 <= i+1 <= e1:
        continue
    else:
        temp.append(blocks[i])
    
blocks = temp
    
temp = []

for i in range(len(blocks)):

    if s2 <= i+1 <= e2:
        continue
    else:
        temp.append(blocks[i])

blocks = temp

print(len(blocks))

for block in blocks:
    print(block)