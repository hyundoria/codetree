n = int(input())

ans = []
visited = [False] * (n+1)

def get(num):

    if num == n+1:
        for row in ans:
            print(row, end=" ")
        print()
        return


    for i in range(1, n+1):

        if visited[i]:
            continue

        visited[i] = True
        ans.append(i)

        get(num+1)
        
        ans.pop()
        visited[i] = False

    return

get(1)