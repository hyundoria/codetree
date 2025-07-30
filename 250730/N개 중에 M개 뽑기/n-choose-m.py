k, n = map(int, input().split())

ans = []

def get(num, t):

    if num == n+1:
        for row in ans:
            print(row, end=" ")
        print()
        return


    for i in range(t, k+1):
        ans.append(i)
        get(num+1, i+1)
        ans.pop()

    return

get(1, 1)