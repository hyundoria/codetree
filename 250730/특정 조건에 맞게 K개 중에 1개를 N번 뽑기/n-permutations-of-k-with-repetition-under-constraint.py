k, n = map(int, input().split())

ans = []

def get(num, i):

    if num == n+1:
        for row in ans:
            print(row, end=" ")
        print()
        return


    for i in range(1, k+1):

        if num == 1 or num == 2 or ans[-1] != i or ans[-2] != i:
            ans.append(i)
            get(num+1, i)
            ans.pop()

    return

get(1, 1)