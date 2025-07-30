k, n = map(int, input().split())

ans = []

def get(num, i):

    if num == n+1:
        for row in ans:
            print(row, end=" ")
        print()
        return


    for i in range(1, k+1):
        ans.append(i)
        get(num+1, i)
        ans.pop()

    return

get(1, 1)