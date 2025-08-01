n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[1] = True

for _ in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

cnt = []

def dfs(vertex):
    
    for curr_v in graph[vertex]:

        if not visited[curr_v]:
            visited[curr_v] = True
            cnt.append(curr_v)
            dfs(curr_v)


dfs(1)
print(len(cnt))