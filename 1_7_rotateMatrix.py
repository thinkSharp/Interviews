def rotateMatrixBy901(m, size):
    n = size - 1
    loop_count = size // 2
    if size % 2 == 1:
        loop_count += 1

    for i in range(0, loop_count):
        for j in range(i, loop_count - i):
            print('i:' + str(i) + " j:" + str(j)  +" , n:" + str(n))
            print(m)
            print(m[i][j], end= ' ')
            print(m[n - i][n - j],end = ' ')
            print( m[n - i][n - j], end = ' ')
            print( m[n - j][j - j])
            m[i][j], m[i + j][n], m[n - i][n - j], m[n - j][j - j] = m[n - j][j - j], m[i][j], m[i+j][n], m[n - i][n - j]
            print(m[i][j], end= ' ')
            print(m[n - i][n - j],end = ' ')
            print( m[n - i][n - j], end = ' ')
            print( m[n - j][j - j])
            print(m)
    return m

def rotateMatrixBy90(m,size):
    for layer in range(0,size//2):
        first = layer
        last = size - 1 - layer
        for j in range(first, last):
            offset = j - first
            top = m[first][j]
            m[first][j] = m[last-offset][first]
            m[last-offset][first] = m[last][last-offset]
            m[last][last-offset] = m[j][last]
            m[j][last] = top
    return m

def test():
    result = rotateMatrixBy90([[1, 2], [3, 4]], 2)
    print(result)
    assert (result == [[3, 1], [4, 2]])

    result = rotateMatrixBy90([[1,2,3],[4,5,6],[7,8,9]], 3)
    print(result)
    assert(result == [[7,4,1],[8,5,2],[9,6,3]])

    result = rotateMatrixBy90([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3)
    print(result)
    assert (result == [[3, 2, 1], [3, 2, 1], [3, 2, 1]])

    result = rotateMatrixBy90([[1, 1, 1,1], [2, 2, 2,2], [3, 3, 3,3],[4,4,4,4]], 4)
    print(result)
    assert (result == [[4,3, 2, 1], [4,3, 2, 1], [4,3, 2, 1], [4,3, 2, 1]])
test()

a = [[4,3, 2], [4,3, 1], [4,2, 1], [3, 2, 1]]
print(len(a))
print(len(a[:1]))
print(len(a[1:]))