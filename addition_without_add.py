def add(v1, v2):
    def xor_carry(b1,b2):
        xor_bs = b1 ^ b2
        and_bs = (b1 & b2) << 1
        if and_bs == 0:
            return xor_bs
        else:
            return xor_carry(xor_bs, and_bs)

    return xor_carry(v1, v2)


def test_add():
    result = add(3,5)
    print(result)

    result = add(13,5)
    print(result)

    result = add(183,1258)
    print(result)
test_add()

b1 = 1
b2 = 2

print((b1 & b2) << 10)