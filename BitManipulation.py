def isSetBit(num, position):
    return num & (1 << position)


def setBit(num, position):
    return num | (1 << position)


def clearBit(num, position):
    return num & ~(1 << position)

def updateBits(n, m, i, j):
    all_ones = ~0
    print(all_ones)
    print(bin(all_ones))
    left = all_ones << (j+1)
    print(left)
    print(bin(left))
    right = (1 << i) - 1
    print(1<<i)
    print(right)
    print(bin(right))
    mask = left | right
    print(-128+3)
    print(mask)
    print(bin(mask))
    print(bin(left & right))
    print(bin(n))
    n_cleared = n & mask
    m_shift = m << i
    print(bin(n_cleared))
    print(bin(m))
    print(bin(m_shift))
    new_val = n_cleared | m_shift
    print(bin(new_val))
    print(new_val)

#updateBits(1024, 19, 2, 6)

def convertBinary(num):
    result = []
    while num > 0:
        r = num % 2
        num = num // 2
        result.insert(0, str(r))
    return ''.join(result)

def decimalToBinary(num):
    result = []
    while num % 2 != 0:
        if num * 2 >= 1:
            result.append('1')
        else:
            result.append('0')

        num = num * 2
        num = num % 1
    str = "." + ''.join(result)
    return str

#print(convertBinary(13))
#print(convertBinary(174))
#print(decimalToBinary(0.75))
#print(decimalToBinary(0.72))

def test():
    a = 1 << 5
    print(bin(a))
    a = a -1
    print(bin(a))

    a = 1 << 5
    print(bin(a))
    b = 1 << 7
    print(bin(b))
    print("c is")
    c = a + b
    print(bin(c))
    mask = ~(1 << 5)
    print(bin(mask))
    print("mask")
    c = c & mask
    print(bin(c))
    mask = ~(1 << 7)
    print(bin(mask))
    c = c & mask
    print(bin(c))
    for i in range(0, 10):
        c = c | 1 << i

    print(bin(c))
    print("to clear most significant bits till 5")
    mask = ( 1 << 5 ) - 1
    print(bin(mask))
    c = c & mask
    print(bin(c))

    print(bin(mask))


    n = int(0b10000000000)
    m  = int(0b10011)
    print("new new new")
    allones = ~0
    print(bin(allones))
    allones = allones << 7
    print(bin(allones))
    print(allones)
    mask = (1 << 2) -1
    print(bin(mask))
    mask2 = allones | mask
    print(bin(mask2))
    print(mask2)
    n_cleared = n & mask2
    print(bin(n_cleared))
    m_shifted = m << 2
    print(bin(m_shifted))
    new = n_cleared | m_shifted
    print(new)

a = 2
b = 3

c = b&a
print(c)