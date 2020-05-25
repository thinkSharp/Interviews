def parens(pren_count):
    def sub_parens(count):
        if count == 0:
            return ""
        subs = sub_parens(count - 1)
        result = set()
        result.add('()')
        for s in subs:
            for i in range(0, len(s)):
                if s[i] == '(':
                    str = s[0:i] + '()' + s[i:]
                    result.add(str)
                    str = s[0:i+1] + '()' + s[i+1:]
                    result.add(str)
                elif s[i] == ')':
                    str = s[0:i+1] + '()' + s[i+1:]
                    result.add(str)
        return result

    res = sub_parens(pren_count)
    return res

def parens_2(count):
    def sub_parens(lst, lef_count, right_count, dic, dic_count, total):
        print("incoming => {0}, {1}, {2}, {3}, {4}".format(lef_count, right_count, dic_count, total, dic))
        if lef_count < 0 or right_count < lef_count:
            return
        if lef_count == 0 and right_count == 0:
            s = ''
            for k,v in dic.items():
                s += v
            lst.append(s)
        else:
            if lef_count > 0:
                dic[dic_count] = '('
                total += 1
                sub_parens(lst, lef_count - 1, right_count, dic, dic_count + 1, total)
            if right_count > lef_count:
                dic[dic_count] = ')'
                total += 1
                sub_parens(lst, lef_count, right_count-1, dic, dic_count+1, total)
    result = []
    sub_parens(result, count, count, {}, 0, 1)
    return result


def test_parens():
    result = parens_2(3)
    print(result)

test_parens()