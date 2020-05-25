def compressString(s1):
    len_s1 = len(s1)
    if len_s1 == 0:
        return s1

    compress_lst = []
    count = 1
    current = s1[0]
    for i in range(1, len_s1):
        if current == s1[i]:
            count += 1
        else:
            compress_lst.append(current)
            compress_lst.append(str(count))
            current = s1[i]
            count = 1
    compress_lst.append(current)
    compress_lst.append(str(count))
    compressed_str = ''.join(compress_lst)

    return compressed_str if len(compressed_str) <= len_s1 else s1

def test():
    result = compressString('aabcccccaaa')
    print(result)
    assert(result == 'a2b1c5a3')

    result = compressString('aabc')
    print(result)
    assert(result == 'aabc')

    result = compressString('')
    print(result)
    assert(result == '')

    result = compressString('AaaabBBBBBcCCCCCd')
    print(result)
    assert(result == 'A1a3b1B5c1C5d1')


test()