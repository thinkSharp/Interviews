def findDiagonalOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    goal: print matrix diagonal order as shown below
    plan:
        1) identify direction of the arror dup and ddown
        2) if dup turn -> move col first, if end of col then move row
        3) if ddown turn -> move row first, if end of row then move column
        4) if dup -> i-1, j+ 1
        5) if ddown -> i+i, j-1

    """
    lr = len(matrix)
    if lr == 0:
        return []
    lc = len(matrix[0])
    total = lc * lr
    result = []
    i, j = 0, 0
    cd = 'u'
    while True:
        if len(result) == total:
            return result
        print("i:{0}, j:{1}, d:{2}".format(i,j,cd))
        if cd == 'u':
            result.append(matrix[i][j])
            if i - 1 < 0 or j + 1 >= lc:
                if j + 1 >= lc:
                    i += 1
                else:
                    j += 1
                cd = 'd'
            else:
                i -= 1
                j += 1

        elif cd == 'd':
            result.append(matrix[i][j])
            if (i + 1) >= lr or (j - 1) < 0:
                if i + 1 >= lr:
                    j += 1
                else:
                    i += 1
                cd = 'u'
            else:
                i += 1
                j -= 1
        print(result)

def test_print():
    result = findDiagonalOrder([[ 1, 2, 3,5 ]])
    print(result)

test_print()