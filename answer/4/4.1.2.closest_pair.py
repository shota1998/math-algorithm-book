import sys
import math

N = int(input())
I = [ [0] * 2 for i in range(N)]
ANSWER = sys.maxsize

for i in range(N):
    x, y = map(int, input().split())
    I[i][0] = x
    I[i][1] = y

for i in range(N):
    for j in range(N):
        if i == j:
            continue
    
        x = pow(I[i][0] - I[j][0], 2)
        y = pow(I[i][1] - I[j][1], 2)
        dist = math.sqrt(x + y)

        ANSWER = min(ANSWER, dist)

print(int(ANSWER))