N = int(input())
A, B = list(map(int, input().split()))

answer = 0

for i in range(N):
    dice = int(input())
    
    if dice in (1, 2):
        answer += A / N
    else:
        answer += B / N

print(answer)
