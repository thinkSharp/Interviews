def sorted_merge(a,b):
    def shift_array_a(index_from):
        for i in range(index_from + 1, len(a)):
            temp = a[i]
            a[i] = a[index_from]
            a[index_from] = temp

    for j in range(0, len(b)):
        for k in range(j, len(a)):
            if a[k] > b[j]:
                shift_array_a(k)
                a[k] = b[j]
                break

    return a

def sorted_merge2(a,b):
    c = a + [0] * len(b)
    c_index = len(c) - 1
    a_index = len(a) - 1
    b_index = len(b) - 1
    while b_index >= 0:
        if a_index >= 0 and a[a_index] >= b[b_index]:
            c[c_index] = a[a_index]
            a_index -=1
        else:
            c[c_index] = b[b_index]
            b_index -=1
        c_index -= 1
    return c

def test_shift_merge():
    result = sorted_merge2([2,4,6,8,10,12,16,18],[1,3,5,7,9])
    print(result)
    assert(result == [1,2,3,4,5,6,7,8,9,10,12,16,18])

test_shift_merge()
