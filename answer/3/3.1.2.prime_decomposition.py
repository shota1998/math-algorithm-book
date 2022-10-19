N = int(input())
LIMIT = int(N ** 0.5)
ANSWER = []

for i in range(2, LIMIT + 1):
    while N % i == 0:
        N /= i
        ANSWER.append(i)

if N >= 2:
    ANSWER.append(int(N))

print(",".join(map(str, ANSWER)))