N = int(input())
A = [int(i) for i in input().split()]

def euclid(left, right):
    remain = 1

    while remain != 0:
        remain = left % right
        left = right
        right = remain

    return left if remain == 0 else 1

left  = A[0] if A[0] > A[1] else A[1]
right = A[1] if A[0] > A[1] else A[0]
remain = euclid(left, right)

for i in range(2, N):
    remain = euclid(remain, A[i])

print(remain)