def subStringCount(n, s):
    result = []
    count = 0
    local_count = 0
    for i in range(0,n):
        str = s[i]
        local_count = 1
        middle = ""
        str_before = ""
        result.append(str)
        for j in range(i+1, n):
            if s[i] == s[j]:
                str += s[j]
                if len(str) > 1 and middle == '':
                    local_count += 1
                    result.append(str)
            else:
                if middle == "":
                    middle = s[j]
                    str_before = str
                    str = ""
                elif str_before != str:
                    break

            if middle != "" and str_before == str:
                result.append(str_before + middle + str)
                local_count += 1
                middle = ""
                str = ""
                str_before = ""
                break
        count += local_count
    return count


print(subStringCount(4, 'aaba'))
print(subStringCount(3, 'aba'))
print(subStringCount(4, 'aaaa'))
print(subStringCount(7,"abcbaba"))
print(subStringCount(9,'aaaabaaaa'))
