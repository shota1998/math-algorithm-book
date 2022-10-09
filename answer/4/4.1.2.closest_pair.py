import sys
import math

N = int(input())
I = [ [0] * 2 for i in range(N)]
ANSWER = sys.maxsize

for i in range(N):
    I[i][0], I[i][1] = map(int, input().split())

for i in range(N):
    for j in range(i+1, N):
        x = pow(I[i][0] - I[j][0], 2)
        y = pow(I[i][1] - I[j][1], 2)
        dist = math.sqrt(x + y)

        ANSWER = min(ANSWER, dist)

print(int(ANSWER))