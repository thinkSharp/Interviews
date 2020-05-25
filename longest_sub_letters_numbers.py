def longest_sub_letters_numbers(lst):
    max_length = 0
    diffs = {}
    n_count = 0
    l_count = 0
    for i in lst:
        if i.isdigit():
            n_count += 1
        else:
            l_count += 1
        diff = abs(n_count - l_count)
        largest_sub = min(n_count, l_count) - diff
        if diff in diffs:
            if diffs[diff] < largest_sub:
                diffs[diff] = largest_sub
                if max_length < largest_sub:
                    max_length = largest_sub
        else:
            diffs[diff] = largest_sub
            if max_length < largest_sub:
                max_length = largest_sub
    return max_length


def longest_sub_2(lst):
    deltas = [0] * len(lst)
    count = 0
    for i in range(0, len(lst)):
        if lst[i].isdigit():
            count += 1
        else:
            count -= 1
        deltas[i] = count

    map = {}
    map[0] = -1
    maxs = [0,0]
    for i in range(0, len(deltas)):
        if deltas[i] not in map:
            map[deltas[i]] = i
        else:
            match = map[deltas[i]]
            distance = i - match
            longest = maxs[1] - maxs[0]
            if distance > longest:
                maxs[1] = i
                maxs[0] = match
    print(maxs)
    return lst[maxs[0]+1: maxs[1]+1]

def test_longest_sub():
    result = longest_sub_2('11a1a')
    print(result)

    result = longest_sub_2('a1aaa1aa11a1a')
    print(result)


#test_longest_sub()

def longest_increase_sub_sequence_recursive(nums):
    len_nums = len(nums)

    def lis_recursive(i, j):
        if i >= len_nums or j >= len_nums:
            return 0
        if (i,j) in memo:
            return memo[(i,j)]
        if nums[i] < nums[j]:
            memo[(i,j)] = 1 + lis_recursive(i+1, j+1)
            return memo[(i,j)]
        else:
            memo[(i,j)] = max(lis_recursive(i+1,j), lis_recursive(i,j+1))
            return memo[(i,j)]

    if len_nums == 0:
        return 0

    memo = {}
    results = {}
    return lis_recursive(0,1)
def test_lissr():
    num = longest_increase_sub_sequence_recursive([1,3,5,4,7,0])
    print(num)
#test_lissr()

def no_longest_increasing_sub_sequence(nums):
    len_nums = len(nums)
    lengths = [0] * len_nums
    counts = [1] * (len_nums)

    for i in range(0, len_nums):
        for j in range(0,i):
            if nums[j] < nums[i]:
                if lengths[j] >= lengths[i]:
                    lengths[i] = 1 + lengths[j]
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
    longest = max(lengths)
    return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    lengths = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[i] >= lengths[j]:
                    lengths[i] = max(1 + lengths[j], lengths[i])
    longest = max(lengths)
    return longest if longest > 0 else 1
def test_lengthOfLIS():
    length = lengthOfLIS([10,9,2,5,3,7,101,18])
    print (length)

#test_lengthOfLIS()

def test_no_of_longest_increasing_sub_sequence():
    num = no_longest_increasing_sub_sequence([4,6,7,7])
    print(num)
    assert (num == 2)
    num = no_longest_increasing_sub_sequence([1,2])
    print(num)
    assert(num == 1)
    num = no_longest_increasing_sub_sequence([1,2,4,3,5,4,7,2])
    print(num)
    assert(num == 3)
    num = no_longest_increasing_sub_sequence([1,3,5,4,7])
    print(num)
    assert(num == 2)
    num = no_longest_increasing_sub_sequence([2,2,2,2,2])
    print(num)
    assert(num == 5)

#test_no_of_longest_increasing_sub_sequence()

