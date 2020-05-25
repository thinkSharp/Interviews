def coinsChanging(coins, total):
    def coins_used(c):
        T = []
        remaining = total
        while True:
            coin = coins[c[remaining]]
            T.append(coin)
            remaining -= coin
            if remaining == 0:
                break
        return T

    len_coins = len(coins)
    if len_coins == 0:
        return 0
    result = [total] * (total + 1)
    used_coins = [-1] * (total + 1)
    possible_coins = []
    result[0] = 0
    for i in range(0, len_coins):
        for j in range(1, total + 1):
            if j >= coins[i]:
                if result[j - coins[i]] + 1 < result[j]:
                    result[j] = 1 + result[j - coins[i]]
                    used_coins[j] = i
                    used = coins_used(used_coins)
                    if used not in possible_coins:
                        possible_coins.append(used)
    return len(possible_coins), coins_used(used_coins), possible_coins


def test():
    result = coinsChanging([7, 2, 3, 6], 13)
    print(result)
    assert (result[0] == 3)

    result = coinsChanging([1, 5, 10, 25], 50)
    print(result)
    assert (result[0] == 35)

    result = coinsChanging([1, 5, 10, 25], 25)
    print(result)
    assert (result[0] == 6)

    result = coinsChanging([1, 5, 10, 25], 100)
    print(result)
    assert (result[0] == 102)
test()
