import sys
def kth_multiply(k):
    array = []
    q3 = []
    q5 = []
    q7 = []
    q3.append(1)

    for i in range(0, k):
        v3 = q3[0]
        v5 = q5[0] if len(q5) > 0 else sys.maxsize
        v7 = q7[0] if len(q7) > 0 else sys.maxsize
        v = min([v3,v5,v7])
        if v == v3:
            q3.remove(v3)
            q3.append(v*3)
            q5.append(v*5)
        elif v == v5:
            q5.remove(v5)
            q5.append(v*5)
        elif v == v7:
            q7.remove(v7)
        q7.append(v*7)
        array.append(v)
    print(array)
    return array[-1]


def test_kth_multiply():
    result = kth_multiply(100)
    print(result)

test_kth_multiply()