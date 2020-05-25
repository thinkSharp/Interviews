T = [[11, 12, 5, 2,1,1], [15, 6,10,1,1,1], [10, 8, 12, 5,1,1], [11, 12, 5, 2,1,1], [11, 12, 5, 1,1,1],[1,1,1,1,1,1]]


def hourglassSum(arr):
    if (len(arr) != 6):
        return 0

    if (len(arr[0]) != 6):
        return 0

    result = []
    r = 0
    c = 0

    for r in range(0,4):
        for c in range(0,4):

            hg = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            print(str(r) + ' ' + str(c) + ' ' + str(hg))
            result.append(hg)

    return max(result)

print(hourglassSum([[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]))

print(hourglassSum([[0, -4, -6, 0, -7, -6],
[-1, -2, -6, -8, -3, -1],
[-8, -4, -2, -8, -8, -6],
[-3, -1, -2, -5, -7, -4],
[-3, -5, -3, -6, -6, -6],
[-3, -6, 0, -8, -6, -7]]))
