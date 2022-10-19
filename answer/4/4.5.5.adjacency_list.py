N, M = map(int, input().split())
R = [0] * (N + 1)
A = 0

for i in range(M):
  a, b = map(int, input().split())

  if a > b:
    R[a] += 1
  if b > a:
    R[b] += 1

for i in range(N):
    if R[i] == 1:
        A += 1

print(A)