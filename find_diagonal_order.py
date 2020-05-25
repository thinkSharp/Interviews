def findDiagonalOrder(nums):
    lr = len(nums)
    if lr == 0:
        return []
    point = []
    for x, row in enumerate(nums):
        for y, n in enumerate(row):
            point.append(((x+y), -x, n))
    return [p[2] for p in sorted(point)]

def findDiagonalOrder2(nums):
    bucket = []
    for x, row in enumerate(nums):
        for y, n in enumerate(row):
            if (x+y) == len(bucket):
                bucket.append([])
            bucket[x+y].append(n)
    for row in bucket:
        row.reverse()
    return [i for row in bucket for i in row]

def test_diagonal_order():
    num = findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(num)
    num = findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    print(num)
    num = findDiagonalOrder2([[1,2,3],[4,5,6],[7,8,9]])
    print(num)
    num = findDiagonalOrder2([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    print(num)
test_diagonal_order()