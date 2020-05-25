def minRemoveToMakeValid(s: str):

    def recursive_min_remove(ln_str, index, open_count, result , max_result):
        if ln_str == index:
            if open_count == 0 and len(result) > 0:
                if len(result) > len(max_result):
                    max_result = result
                return True
            else:
                return False
        else:
            ch = s[index]

            if ch != '(' and ch != ')':
                result.append(ch)
                ret = recursive_min_remove(ln_str, index + 1, open_count, result, max_result)
            else:
                ret = recursive_min_remove(ln_str, index + 1, open_count, result, max_result)

                if ch == '(':
                    result.append('(')
                    ret |= recursive_min_remove(ln_str, index + 1, open_count + 1, result, max_result)
                elif ch == ')' and open_count > 0:
                    result.append(')')
                    ret |= recursive_min_remove(ln_str, index + 1, open_count - 1, result, max_result)
            #memo[index] = ret
        return ret

    ln = len(s)
    memo = {}
    res = []
    recursive_min_remove(ln, 0, 0, [], res)
    return ''.join(res) if len(res) > 0 else ''

def test_max():
    res = minRemoveToMakeValid("lee(t(c)o)de)")
    print(res)

test_max()