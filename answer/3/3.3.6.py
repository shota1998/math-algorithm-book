N = int(input())
A = list(map(int, input().split()))
MAX      = 100000
MAX_HALF = MAX / 2

count = [0 for i in range(MAX)]

for i in range(N):
    count[A[i]] += 1

answer = 0
for i in range(1, MAX_HALF):
    answer += [count[i]] * count[MAX - i]

# Combinations below. rCn
# n = MAX_HALF
# r = 2
answer += count[MAX_HALF] * (count[MAX_HALF] - 1) // 2

print(answer)