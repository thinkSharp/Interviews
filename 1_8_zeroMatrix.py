def fillZeros(m):
    len_row = len(m)
    len_column = len(m[0])
    zero_rows = []
    zero_columns = []

    for i in range(0, len_row):
        for j in range(0, len_column):
            if m[i][j] == 0:
                zero_rows.append(i)
                zero_columns.append(j)

    for i in range(0, len_row):
        for j in range(0, len_column):
            if i in zero_rows:
                m[i][j] = 0
            if j in zero_columns:
                m[i][j] = 0
    return m


def test():
    result = fillZeros([[1, 2], [3, 0]])
    print(result)
    assert (result == [[1, 0], [0, 0]])
    result = fillZeros([[1, 0, 3], [3,1, 0]])
    print(result)
    assert (result == [[0,0, 0], [0,0, 0]])


test()
