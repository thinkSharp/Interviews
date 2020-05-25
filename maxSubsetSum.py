def maxSubsetSum1(arr):
    result = [0] * len(arr)

    for i in range(0, len(arr)):
        result[i] = (arr[i], arr[i], i, i)
        for j in range(i - 1, -1, -1):
            if i - result[j][2] > 1:
                new_sum = result[j][0] + result[i][0]
                if result[j][0] < new_sum:
                    result[j] = new_sum, result[j][1], i, result[j][3]
            elif i - result[j][3] > 1:
                new_sum = result[j][1] + result[i][0]
                if result[j][0] < new_sum:
                    result[j] = new_sum, result[j][0], i, result[j][2]

    return max([max(i, j) for i, j, k, l in result])

def maxSubsetSum2(arr):
    arr_len = len(arr) + 1
    memo = [[0] * arr_len for i in range(0, arr_len)]
    max_sub = 0
    j = 1
    for i in range(1, arr_len):
        j = max(1, i-2)
        if j < i:
            memo[i][j] = memo[i - 1][j]
        elif j == i:
            memo[i][j] = arr[j - 1] if arr[j - 1] > memo[i - 1][j] else memo[i - 1][j]
        elif j == i +1:
           memo[i][j] = arr[j]
        else:
          memo[i][j] = max(arr[j - 1] + memo[i][j - 2], arr[j - 1] + memo[i][j - 3], memo[i][j - 2])
        if max_sub < memo[i][j]:
          max_sub = memo[i][j]

    return max_sub


def maxSubsetSum(arr):
 arr_len = len(arr)
 result = [i for i in arr]

 for i in range(1, arr_len - 1):
  if result[i - 1] > result[i]:
   result[i] = result[i - 1]
  result[i + 1] = max(result[i + 1], result[i - 1], result[i - 1] + result[i + 1])
 return max(result)


def test():
    resp = maxSubsetSum([3, 7, 4, 6, 5])
    print(resp)
    assert (resp == 13)

    resp = maxSubsetSum([3, 5, -7, 8, 10])
    print(resp)
    assert (resp == 15)

    resp = maxSubsetSum([3, 5, -7, 8, 10, -20, -40, -50, -60, 80])
    print(resp)
    assert (resp == 95)

test()

