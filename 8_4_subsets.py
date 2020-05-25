def getsubsets(lst):
    result = []
    base = [[]]
    for item in lst:
        for sub_item in base:
            if sub_item is None:
                result.append([item])
            else:
                result.append(sub_item + [item])
        base = list(result)
    return result


def test_subsets():
    items = [1,2,3,4,5]
    result = getsubsets(items)
    print(result)


test_subsets()