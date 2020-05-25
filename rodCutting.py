##
# Given a rod of length n inches and an array of prices that contains size smaller then n,
# determine the max value
# time complexity O(p * r)
# space complexity same
##

def rodCutting(prices, rod):
    len_rod = rod + 1
    prices.insert(0, 0)
    result = [[0] * len_rod for i in range(0, len(prices))]

    for i in range(1, len(prices)):
        for j in range(1, len_rod):
            if j < i:
                result[i][j] = result[i - 1][j]
            else:
                price = prices[i]
                result[i][j] = max(result[i - 1][j], result[i][j - i] + price)
    return result


def rodCuttingImproveSpace(prices, rod):
    len_rod = rod + 1
    result = [0 for i in range(0, len_rod)]
    prices.insert(0, 0)
    for i in range(1, len(prices)):
        for j in range(1, len_rod):
            if j >= i:
                result[j] = max(result[j], prices[i] + result[j - i])
    return result


print(rodCuttingImproveSpace([2, 5, 7, 8], 5))
print(rodCutting([2, 5, 7, 8], 5))
