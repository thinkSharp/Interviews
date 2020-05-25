def flipBitToWin(num):
    bin_num = str(bin(num))
    print(bin_num)
    bin_num = bin_num[2:]
    left_ones = 0
    right_ones = 0
    is_left = True
    max_ones = 0
    for i in bin_num:
        if i == '1':
            if is_left:
                left_ones += 1
            else:
                right_ones += 1
        else:
            if not is_left:
                ones = left_ones + right_ones + 1
                if max_ones < ones:
                    max_ones = ones
                left_ones = right_ones
                right_ones = 0
            else:
                is_left = False
    ones = left_ones + right_ones + 1
    if max_ones < ones:
        max_ones = ones
    return max_ones

def bitSwapRequired(a, b):
    c = a^b
    print(bin(a))
    print(bin(b))
    print(bin(c))
    count = 0
    while c != 0:
        count += c & 1
        c = c >> 1
        print(bin(c))

    return count

#print(bitSwapRequired(29,15))
#print(bitSwapRequired(4,3))


def test_flip():
    print(flipBitToWin(1775))
    print(flipBitToWin(23))
    print(flipBitToWin(230))
    print(flipBitToWin(1024))
    print(flipBitToWin(15))
#test_flip()

def rshift(val, n):
    num = (1 << 32)
    print(num)
    print(bin(num))
    print(hex(num))
    print(bin(0xaaaaaaaa))
    print(bin(0x55555555))
    res = val % (1 << 32)
    res = res >> n
    return res
    #return (val % 0x100000000) >> n

def swapOddEvenBits(num):
    print(bin(num))
    x = num & 0xaaaaaaaa
    print(bin(x))
    x = x >> 1
    print(bin(x))
    y = num & 0x55555555
    print(bin(y))
    y = y << 1
    print(bin(y))
    x = x | y
    print(bin(x))
print(int(0b1010))
swapOddEvenBits(10)

#print(rshift(-1000, 3))
#print(-1000 >> 3)