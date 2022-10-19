N , M = map(int, input().split())
G = [[False] * N for i in range(N)]
D = [-1] * N
Q = []

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = True
    G[b][a] = True


Q.append(0)
D[0] = 0

while len(Q) > 0:
    pos = Q[0]
    Q.pop(0)
    for next, value in enumerate(G[pos]):
        if value == True and D[next] == -1:
            D[next] = D[pos] + 1
            Q.append(next)

print(D)
