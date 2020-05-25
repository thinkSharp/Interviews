def replaceSpace(str, str_ln):
    len_str = len(str)
    new_arr = [''] * len_str
    j = 0
    for i in range(0,str_ln):
        if str[i] == ' ':
            new_arr[j] = '%'
            new_arr[j + 1] = '2'
            new_arr[j + 2] = '0'
            j += 3
        else:
            new_arr[j] = str[i]
            j += 1
    return ''.join(new_arr)


def test():
    result = replaceSpace("Mr John Smith      ", 13)
    print(result)
    assert (result == "Mr%20John%20Smith")


test()
