def knapsack(profits, weights, capacity):
    memo = {}
    max_profit = 0
    lw, lp = len(weights), len(profits)
    def recursive(index, p, rem):
        nonlocal max_profit
        if index == lw or rem == 0:
            if max_profit < p:
                max_profit = p
                memo[index] = max_profit
            return max_profit
        if index in memo:
            return memo[index]

        if rem - weights[index] >= 0:
            include = recursive(index + 1, p + profits[index], rem - weights[index])
            memo[index] = include
        else:
            memo[index] = memo[index-1]
        return memo[index]
    #memo[0] = 0
    return recursive(0, 0, capacity)

s = 'babad'
print(s[0:4])
print(s[0:4][::-1])