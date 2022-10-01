from sys import stdin

N = int(stdin.readline().rstrip())
A = [int (x) for x in stdin.readline().rstrip().split()]


def euclid(numerator, denominator):
    remainder = 2

    while remainder > 1 or remainder != 0:
        remainder   = numerator % denominator
        numerator   = denominator
        denominator = remainder
    
    return numerator if remainder == 0 else 1
        

def main():
    numerator   = A[0] if A[0] >= A[1] else A[1] 
    denominator = A[1] if A[0] >= A[1] else A[0]
    remainder   = euclid(numerator, denominator)

    for i in range(2, N):
        remainder = euclid(remainder, A[i])

    print(remainder)

main()
