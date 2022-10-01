N = int(input())
A = [int(x) for x in input().split()]
PRICE = 500

def count_each_price():
    result = {}
    for x in A:
        if x not in result.keys():
            result.setdefault(x, 1)
        else:
            result[x] += 1
    
    return result

def get_combinations_price(prices):
    result = {}
    for x in A:
        remain = 500 - x
        if remain in prices.keys() and remain not in result.keys():
            result.setdefault(x, remain)
    
    return result

def get_combinations_goods(combinations_prices, prices):
    result = 0
    for a, b in combinations_prices.items():
        result += prices[a] * prices[b]

    return result

def main():
    prices = count_each_price()
    combinations_prices = get_combinations_price(prices)
    combinations_goods =  get_combinations_goods(combinations_prices, prices)
    print(combinations_goods)

main()