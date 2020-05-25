def arrayManipulation1(n, queries):
    max_value = 0
    lst = [0] * (n + 1)
    for q in queries:
        start, end, value = q
        for i in range(start, end + 1):
            lst[i] += value

            if max_value < lst[i]:
                max_value = lst[i]

    return max_value


def arrayManipulation(n, queries):
    lst = []
    for q in queries:
        start, end, value = q
        lst.append(set(i for i in range(start, end + 1)))
    inter = set.intersection(*lst)
    return inter


def arrayManipulation2(n, queries):
    lst = [0] * (n + 1)
    for q in queries:
        x, y, value = q

        lst[max(x - 1, 0)] += value
        if y <= len(lst): lst[y] -= value
    m = x = 0
    for i in lst:
        x = x + i
        if m < x: m = x
    return m


print(arrayManipulation2(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
