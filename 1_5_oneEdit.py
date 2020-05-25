def isOneEditAway(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    i = 0
    j = 0
    s1 = s1.lower()
    s2 = s2.lower()
    one_edit = False
    while True:
        if i >= len_s1 and j >= len_s2:
            break
        if i >= len_s1 or j >= len_s2:
            if abs(len_s2 - len_s1) == 1 and not one_edit:
                return True

            return False
        if s1[i] == s2[j]:
            i += 1
            j += 1
            continue
        else:
            if one_edit:
                return False
            one_edit = True
            if len_s1 == len_s2: # replace
                i += 1
                j += 1
            elif len_s1 < len_s2: # remove
                j += 1
            else:                  # insert
                i += 1

    return True


def test():
    result = isOneEditAway('pale', 'ple')
    print(result)
    assert (result == True)

    result = isOneEditAway('pales', 'pale')
    print(result)
    assert (result == True)

    result = isOneEditAway('pale', 'bale')
    print(result)
    assert (result == True)

    result = isOneEditAway('pales', 'ble')
    print(result)
    assert (result == False)

test()