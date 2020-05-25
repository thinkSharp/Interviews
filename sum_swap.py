def sum_swap(lst1, lst2):
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    diff = (sum1 - sum2) // 2

    if (sum1 - sum2) % 2 != 0:
        return []

    set_lst2 = set(lst2)

    for i in lst1:
        two = i - diff
        if two in set_lst2:
            return i, two
    return []


def test_sum_swap():
    result = sum_swap([4,1,2,1,1,2],[3,6,3,3])
    print(result)
    assert(result == (1,3) or result == (4, 6))

    result = sum_swap([4,1,2,1,1,2],[3,6,3,3])
    print(result)
    assert(result == (1,3) or result == (4, 6))
test_sum_swap()