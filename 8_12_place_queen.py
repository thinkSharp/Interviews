def validate_position(columns, row, column):
    for row2 in range(0, len(columns)):
        column2 = columns[row2]

        if column2 == column:
            return False

        column_distance = abs(column2 - column)
        row_distance = abs(row2 - row)

        if column_distance == row_distance:
            return False

    return True


def place_queen(size):
    def place_queen_per_column(row, columns, result):
        #
        print("Incoming => {0}, {1}".format(row, columns))
        if row == size-1:
            result.append(columns)
        else:
            for column in range(0, len(columns)):

                if validate_position(columns, row, column):
                    columns[row] = column
                    #print("columns => {0}, {1}, {2}".format(column, row, columns))
                    place_queen_per_column(row + 1, columns, result)

    res = []
    cols = [20] * size
    place_queen_per_column(0, cols, res)
    res[0][size-1] = 0
    return res


def test_placing_queen():
    result = place_queen(8)
    print(result)


test_placing_queen()
