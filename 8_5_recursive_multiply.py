def recursive_multiply(a1, b1):
    def rec_multiply1(a,b,count):
        if b <= 0:
            return 0, count
        elif b == 1:
            return a, count + 1
        r, count = rec_multiply1(a, b-1, count)
        count += 1
        r += a
        return r, count

    if a1 < b1:
        a1, b1 = b1, a1
    return rec_multiply1(a1,b1, 0)


def recursive_multiply_minimum(a1, b1):
    def rec_multiply(a,b,count):
        if b <= 0:
            return 0, count
        elif b == 1:
            return a, count + 1

        b2 = b >> 1
        r, count = rec_multiply(a, b2, count)
        if b % 2 == 0:
            count += 2
            r = r + r
            return r, count
        else:
            count += 3
            r = r + r + a
            return r, count
    if a1 < b1:
        a1, b1 = b1, a1
    return rec_multiply(a1,b1, 0)


def test_recursive_multiply():

    result = recursive_multiply_minimum(13, 15)
    print(result)

    result = recursive_multiply_minimum(4, 5)
    print(result)

    result = recursive_multiply_minimum(400, 500)
    print(result)

    result = recursive_multiply(13, 15)
    print(result)

    result = recursive_multiply(4, 5)
    print(result)

    result = recursive_multiply(400, 500)
    print(result)

    print(bin(3 >> 1))
    print(bin(2 >> 1))


test_recursive_multiply()