def coins_chain_recursive(n):
    coins = [25,10,5,1]
    def make_chang(amount, index):
        if index >= len(coins) - 1:
            return 1
        denom_amount = coins[index]
        ways = 0
        i = 0
        while denom_amount * i <= amount:
            used = amount - denom_amount * i
            ways += make_chang(used, index + 1)
            i += 1

        return ways
    return make_chang(n, 0)

def coins_chain_top_down(n):
    result = [0] * (n + 1)
    coins = [25,10,5,1]
    total = 0
    for coin in coins:
        for j in range(1, (n+1)):
            if j == coin:
                result[j] = 1 + result[j - coin]
                if j == n:
                    total += 1
            elif j > coin:
                result[j] = min(result[j], result[j-1] + result[coin])
                if result[j] == n:
                    total += 1
            else:
                result[j] = result[j-1]
    return total



def test_coins_chain():
    result = coins_chain_recursive(100)
    result2 = coins_chain_top_down(100)
    print(result, end=' ')
    print(result2)
    assert(result == result2)

test_coins_chain()