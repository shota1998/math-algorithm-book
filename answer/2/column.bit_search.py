from sys import stdin


N, S = [int(x) for x in stdin.readline().rstrip().split()]
A    = [int(x) for x in stdin.readline().rstrip().split()]


def bit_search():
    for i in range(1 << N):
        sum = 0

        for j in range(1, N + 1):
            if (i & (1 << j - 1)) != 0:
                sum += A[j - 1]

        if sum == S:
            return True
    
    return False


def main():
    if bit_search():
        print("Yes")
    else:
        print("No")
        

main()