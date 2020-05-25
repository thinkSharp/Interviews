def contiguous_sequence(lst):
    max_sum = -1
    max_point = -1, -1

    if len(lst) == 0:
        return max_point

    running_sum = 0
    running_start = 0
    running_end = 0
    for i in range(0, len(lst)):
        old_sum = running_sum
        running_sum = running_sum + lst[i]

        if running_sum < lst[i]:
            running_sum = lst[i]
            running_start = i
            running_end = i
        elif running_sum > old_sum:
            running_end = i

        if max_sum < running_sum:
            max_sum = running_sum
            max_point = running_start, running_end

    return max_sum, max_point


def test_contiguous_sequence():
    result = contiguous_sequence([2, -8, 3, -2, 4, -10])
    print(result)
    assert(result[0] == 5)
    assert(result[1] == (2,4))
    result = contiguous_sequence([2, -8, 3, -2, 4, -10, 5,7,-5,-3])
    print(result)
    assert(result[0] == 12)
    assert(result[1] == (6,7))
    result = contiguous_sequence([2, -8, 3, -2, 4, -10, 5,7,-5,100])
    print(result)
    assert(result[0] == 107)
    assert(result[1] == (6,9))

test_contiguous_sequence()