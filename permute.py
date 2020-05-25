def permute_unique(nums):
    def rec(combine, remains):
        if len(remains) == 0:
            output.append(combine[:])
        else:
            for i, num in enumerate(remains):
                if i > 0 and remains[i-1] == remains[i]:
                    continue
                rec(combine + [num], remains[:i]+remains[i+1:])

    n = len(nums)
    if n == 0:
        return []
    output = []
    rec([], nums)
    return output

def permute(nums):
    def rec(combine, remains):
        if len(remains) == 0:
            output.append(combine[:])
        else:
            for i, num in enumerate(remains):
                rec(combine+[num], remains[:i] + remains[i+1:])
    n = len(nums)
    if n == 0:
        return  []
    output = []
    rec([],nums)
    return output

def test_permute_unique():
    ret = permute_unique([1,1,2,2])
    print(ret)
    ret = permute([1,2,3])
    print(ret)

#test_permute_unique()

def subset(nums):
    result = [[]]
    for i, num in enumerate(nums):
        result += [curr + [num] for curr in result]
    return result

def subsets(nums):
    def backtrack(first=0, curr=[]):
        if len(curr) == k:
            output.append(curr[:])
        for i in range(first, n):
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output

def subset_backtrack(nums):
    def back_track(index = 0, curr = []):
        if k == len(curr):
            output.append(curr[:])
        for i in range(index, n):
            curr.append(nums[i])
            back_track(i + 1, curr)
            curr.pop()

    n = len(nums)
    if n == 0:
        return []
    output = []
    for k in range(n+1):
        back_track()

    return output

def test_subset():
    num = subset([1,2,3])
    print(num)
    num = subset_backtrack([1,2,3])
    print(num)

#test_subset()

def findall_strobogrammatic(number):
    def all_strobo_grammtic(n, m, start_ends):
        if n == 0: return ['']
        if n == 1: return ['0','1','8']

        result = []
        strbo = all_strobo_grammtic(n-2, m, start_ends)
        for index, (s,e) in enumerate(start_ends):
            if n == m and index == 0: continue
            new = [s + strb + e for strb in strbo]
            result.extend(new)
        return result
    if number == 0:
        return ['']
    se = [('0','0'),('1','1'),('8','8'),('6','9'),('9','6')]
    return all_strobo_grammtic(number, number, se)

def test_strbogrammatic():
    num = findall_strobogrammatic(5)
    print(num)

test_strbogrammatic()


