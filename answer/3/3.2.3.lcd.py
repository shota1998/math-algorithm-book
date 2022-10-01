# https://univ-juken.com/saisyo-kobaisu#:~:text=%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0%E3%82%92%E6%B1%82%E3%82%81%E3%82%8B%E3%81%AB,%E5%85%AC%E5%80%8D%E6%95%B0%E3%81%8C%E6%B1%82%E3%82%81%E3%82%89%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82

from sys import stdin

N = int(stdin.readline().rstrip())
A = [int (x) for x in stdin.readline().rstrip().split()]


def get_gcd(numerator, denominator):
    remainder = 2

    while remainder > 1 or remainder != 0:
        remainder   = numerator % denominator
        numerator   = denominator
        denominator = remainder
    
    return numerator if remainder == 0 else 1
        
def get_lcd(numerator, denominator):
    gcd = get_gcd(numerator, denominator)
    return int(numerator * denominator / gcd)

def main():
    numerator   = A[0] if A[0] >= A[1] else A[1] 
    denominator = A[1] if A[0] >= A[1] else A[0]
    lcd         = get_lcd(numerator, denominator)

    for i in range(2, N):
        lcd = get_lcd(lcd, A[i])

    print(lcd)

main()
