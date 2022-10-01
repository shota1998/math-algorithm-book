N = int(input())
A = [int(x) for x in input().split()]
R = 2

def count_numbers():
    result = {}
    for x in A:
        if x in result.keys():
            result[x] += 1
        else:
            result.setdefault(x, 1)
    
    return result

def calc_factorial(x):
    result = 1
    while (x > 0):
        result *= x
        x -= 1
    
    return result

def calc_permutations(n):
    numerator = calc_factorial(n)
    denominator = calc_factorial(n - R)
    return numerator / denominator

def calc_combinations(n):
    numerator = calc_permutations(n)
    denominator = calc_factorial(R)
    return int(numerator / denominator)

def main():
    count = count_numbers()

    result = 0
    for number in count.values():
        result += calc_combinations(number)

    print(result)
        

main()