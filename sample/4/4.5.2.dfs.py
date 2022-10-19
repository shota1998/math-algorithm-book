N, M = map(int, input().split())
G = [[False] * N for i in range(N)]
Visited = [False] * N
Answer = True

def dfs(pos):
    Visited[pos] = True
    for key, value in enumerate(G[pos]):
        if value == True and Visited[key] == False:
            dfs(key)


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = True
    G[b][a] = True

dfs(0)


for i in Visited:
    if i == False:
        Answer = False


if Answer == True:
    print("Yes")
else:
    print("No")