def minimumJump(arr):
    len_arr = len(arr)
    if len_arr == 0:
        return 0, [], []
    result = [len_arr] * len_arr
    track = [len_arr] * len_arr
    result[0] = 0
    track[0] = 0
    for i in range(0, len_arr):
        for j in range(0, i):
            if i <= j + arr[j]:
                result[i] = min(result[i], 1 + result[j])
                track[i] = min(j, track[i])

    return result[len(arr) -1], result, track


def test():
    result = minimumJump([2,3,1,1,2,4,2,0,1,1])
    print(result)
    assert(result[0] == 4)
    result = minimumJump([])
    print (result)
    assert(result[0] == 0)
test()