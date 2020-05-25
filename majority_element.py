def majority_element(lst):
    majority = 0
    count = 0
    for i in lst:
        if count == 0:
            majority = i
        if i == majority:
            count += 1
        else:
            count -= 1
    count = 0
    for i in lst:
        if i == majority:
            count += 1
    return majority if (len(lst) // 2) < count else -1


def test_majority_element():
    number = majority_element([1,2,5,9,5,9,5,5,5])
    print(number)
    number = majority_element([3,1,7,7,3,7,3,7,1,7,7])
    print(number)


test_majority_element()