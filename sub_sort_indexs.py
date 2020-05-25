import sys


def sub_sort_indexes(lst):
    min_index = len(lst)
    max_index = 0
    min_value = sys.maxsize
    max_value = -1

    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i] and lst[i] < min_value:
            min_value = lst[i]
            min_index = i
            if max_value < lst[i]:
                max_value = lst[i]
                max_index = i

    for i in range(len(lst)-1, -1, -1):
        if max_value > lst[i]:
            max_index = i
            break

    for i in range(0, len(lst)):
        if min_value < lst[i]:
            min_index = i
            break

    return min_index , max_index


def test_sub_sort_indexes():
    result = sub_sort_indexes([1,2,3,4,7,10,12,7,6,13,6,16,18,19])
    print(result)
    assert(result == (4,10))
    result = sub_sort_indexes([2,3,4,1,5,6,7,8,9])
    print(result)
    assert(result == (0,3))
    result = sub_sort_indexes([2,9,4,1,5,6,7,8,3])
    print(result)
    assert(result == (0,8))
    result = sub_sort_indexes([1,2,3,4,7,10,12,7,6,13,16,18,19])
    print(result)
    assert(result == (4,8))
test_sub_sort_indexes()