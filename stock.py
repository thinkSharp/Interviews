import sys


def stock_buy_sell_one_time(prices):
    len_prices = len(prices)
    if len_prices == 0:
        return 0
    max_profit = 0
    min_price = sys.maxsize

    for i in range(len_prices):
        if prices[i] < min_price:
            min_price = prices[i]
        elif max_profit < prices[i] - min_price:
            max_profit = prices[i] - min_price
    return max_profit


def stock_buy_sell_one_time_optimized(prices):
    len_prices = len(prices)
    if len_prices == 0:
        return 0

    max_profit = 0
    min_price = float('inf')
    for i in range(len_prices):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


def test_one_transaction():
    profit = stock_buy_sell_one_time([7, 1, 5, 3, 6, 4])
    print(profit)
    assert (profit == 5)
    profit = stock_buy_sell_one_time([2, 1, 4])
    print(profit)
    assert (profit == 3)
    profit = stock_buy_sell_one_time_optimized([7, 1, 5, 3, 6, 4])
    print(profit)
    assert (profit == 5)
    profit = stock_buy_sell_one_time_optimized([2, 1, 4])
    print(profit)
    assert (profit == 3)


# test_one_transaction()

def buy_sell_multiple_transactions(prices):
    len_prices = len(prices)
    if len_prices == 0:
        return 0
    min_price = sys.maxsize
    max_profit = 0
    current_profit = 0
    for price in prices:
        if current_profit < price - min_price:
            current_profit = price - min_price
        else:
            min_price = price
            max_profit += current_profit
            current_profit = 0
    max_profit += current_profit
    return max_profit


def buy_sell_multiple_transactions_optimized(prices):
    len_prices = len(prices)
    if len_prices == 0:
        return 0

    min_price = sys.maxsize
    max_profit = 0
    current_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        current_profit = max(current_profit, price - min_price)
        max_profit = max(max_profit, max_profit + current_profit)
    return max_profit


def test_multi_transactions():
    profit = buy_sell_multiple_transactions([7, 1, 5, 3, 6, 4])
    print(profit)
    assert (profit == 7)
    profit = buy_sell_multiple_transactions([2, 1, 4])
    print(profit)
    assert (profit == 3)
    # profit = buy_sell_multiple_transactions_optimized([7,1,5,3,6,4])
    # print(profit)
    # assert(profit == 7)
    # profit = buy_sell_multiple_transactions_optimized([2,1,4])
    # print(profit)
    # assert(profit == 3)


# test_multi_transactions()

def max_profit_two_transactions_dynamic(prices):
    len_prices = len(prices)
    if len_prices == 0:
        return 0

    profit_left = [0] * len_prices
    profit_right = [0] * len_prices
    max_profit = 0
    min_price = float('inf')
    for i in range(len_prices):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        profit_left[i] = max_profit
    max_price = 0
    max_profit = 0
    for i in range(len_prices - 1, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price - prices[i])
        profit_right[i] = max_profit
    best_profit = 0
    print(profit_right)
    print(profit_left)
    for i in range(0, len_prices):
        if i == len_prices - 1:
            best_profit = max(best_profit, profit_left[i])
        else:
            best_profit = max(best_profit, profit_left[i] + profit_right[i + 1])
    return best_profit


def max_profit_two_transactions_optimized(prices):
    t1_cost = float('inf')
    t2_cost = float('inf')
    t1_profit = 0
    t2_profit = 0
    for price in prices:
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)

        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)
    return t2_profit


def test_max_profit_two_transactions():
    profit = max_profit_two_transactions_optimized([1, 2, 3, 4, 5])
    print(profit)
    profit = max_profit_two_transactions_optimized([7, 1, 5, 3, 6, 4])
    print(profit)
    profit = max_profit_two_transactions_optimized([2, 1, 4])
    print(profit)
    profit = max_profit_two_transactions_optimized([2, 1, 4, 3, 5, 7, 9, 2, 4])
    print(profit)
    profit = max_profit_two_transactions_dynamic([1, 2, 3, 4, 5])
    print(profit)
    profit = max_profit_two_transactions_dynamic([7, 1, 5, 3, 6, 4])
    print(profit)
    profit = max_profit_two_transactions_dynamic([2, 1, 4])
    print(profit)
    profit = max_profit_two_transactions_dynamic([2, 1, 4, 3, 5, 7, 9, 2, 4])
    print(profit)


# test_max_profit_two_transactions()

def max_buy_sell_k_times(prices, k):
    len_prices = len(prices)
    if k == 0 or len_prices == 0:
        return 0

    current = [0] * (k + 1)
    for i in range(1, k + 1):
        max_diff = 0-prices[0]
        for j in range(1, len_prices):
            max_diff = max(max_diff, current[i-1] - prices[j])
            current[i] = max(current[i], max_diff + prices[j])

    return current[-1]


def maxProfit(prices, k):
    if k > len(prices) >= 1:
        return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] > prices[i])
    cash, asset = [float('-inf')] * (k + 1), [0] * (k + 1)
    for price in prices:
        for i in range(1, k + 1):
            cash[i] = max(cash[i], asset[i - 1] - price)
            asset[i] = max(asset[i], cash[i] + price)
    return asset[k]


def test_max_buy_sell_k_times():
    profit = maxProfit([1,2,3,0,2], 2)
    print(profit)
    profit = max_buy_sell_k_times([1,2,3,0,2], 2)
    print(profit)
    profit = max_buy_sell_k_times([2, 5, 7, 1, 4, 3, 1, 3], 3)
    print(profit)
    profit = max_buy_sell_k_times([2, 4, 1], 2)
    print(profit)


#test_max_buy_sell_k_times()

def maxProfit_with_cooldown(prices):
    len_prices = len(prices)
    if len_prices < 2:
        return 0

    dp = [[0, 0] for _ in range(len_prices)]
    dp[0][1] = - prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], -prices[1])

    for i in range(2, len_prices):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    return dp[len_prices - 1][0]

def test_max_profit_with_cooldown():
    result = maxProfit_with_cooldown([1,2,3,0,2])


def maxProfit(k, prices):
    if k >= len(prices)//2:
        return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i-j > 0)
    hold, release = [float('-inf')]*(k+1), [0]*(k+1)
    for p in prices:
        for i in range(1, k+1):
            print(release)
            print(hold)
            release[i] = max(release[i], hold[i]+p)
            hold[i] = max(hold[i], release[i-1]-p)

    return release[k]

def test_max_profit():
    result = maxProfit(2, [3,2,6,5,0,3])
    print(result)
test_max_profit()