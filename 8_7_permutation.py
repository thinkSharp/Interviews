import collections

def permutation(s1):
    def permutation_sub(s, sub_s):
        result = []
        n = len(s)
        if n >= 2:
            r1 = permutation_sub(s[0: n-1], [s[n-1]])
            for r in r1:
                for i in range(0, len(r)):
                    res = r[:i] + sub_s + r[i:]
                    result.append(res)
            return result
        else:
            return [s + sub_s, sub_s + s]


    lst = [s for s in s1]
    ln = len(lst)
    if ln< 2:
        return [lst]
    return permutation_sub(lst[0:ln-1], [lst[ln-1]])


def permutationWithOutDup(s2):
    def permutation_sub(dit, prefix, remaining, result):
        print("Input = {0}, {1}, {2}, {3}".format(dit,prefix,remaining,result))
        if remaining == 0:
            result.append(prefix)
            return
        for k,v in dit.items():
            if v > 0:
                dit[k] = v - 1
                permutation_sub(dit, prefix + k, remaining -1, result)
                dit[k] = v
        return
    dict = collections.Counter(s2)
    result = []
    permutation_sub(dict, '', len(s2), result)
    return result



def test_unique_permutation():
    result = permutationWithOutDup('aab')
    print(result)

test_unique_permutation()

def test_non_unique_permutation():
    result = permutation('aba')
    print(result)
    result = permutation('ab')
    print(result)
    result = permutation('abcdefg')
    print(result)


test_non_unique_permutation()
