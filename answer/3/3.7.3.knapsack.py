N, W = [int(x) for x in input().split()]
N += 1
W += 1
w = [0]
v = [0]
DP = [[0] * W for x in range(N)]
MINIMUM = -1

for x in range(N-1):
    tmp_w, tmp_v = [int(x) for x in input().split()]
    w.append(tmp_w)
    v.append(tmp_v)

DP[0][0] = 0
for x in range(1, W):
    DP[0][x] = MINIMUM

for i in range(1, N):
    for j in range(W):
        if j < w[i]:
            DP[i][j] = DP[i-1][j]
        if j >= w[i]:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i]] + v[i])

answer = 0
for i in range(W):
    answer = max(answer, DP[N-1][i])

print(answer)