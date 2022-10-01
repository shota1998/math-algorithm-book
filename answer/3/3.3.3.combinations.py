from sys import stdin

N, R = [int(x) for x in stdin.readline().rstrip().split()]

def calc_factorial(x):
    result = 1
    while (x > 0):
        result *= x
        x -= 1
    
    return result

def calc_permutation():
    numerator = calc_factorial(N)
    denominator = calc_factorial(N - R)
    return numerator / denominator

def calc_combinations():
    numerator = calc_permutation()
    denominator = calc_factorial(R)
    return int(numerator / denominator)

def main():
    print(calc_combinations())

main()