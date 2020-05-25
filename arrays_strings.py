import collections


def lengthOfLongestSubstring(s):
    ln = len(s)
    if ln == 0:
        return 0
    char_map = collections.defaultdict(int)
    start, end, ans = 0, 0, 0
    while start < ln and end < ln:
        if s[end] not in char_map:
            char_map[s[end]] = end
            end += 1
            ans = max(ans, (end - start))

        else:
            del char_map[s[end]]
            start += 1

    return ans


def lengthOfLongestSubstring1(s):
    ln = len(s)
    if ln == 0:
        return 0

    start, max_length = 0, 0

    seen = collections.defaultdict(int)
    lst = list(s)
    for end in range(ln):
        if lst[end] not in seen:
            new_length = (end - start) + 1
            print("new:{0}, start:{1}, end:{2}".format(new_length, start, end))
            if new_length > max_length:
                max_length = new_length
        else:
            if seen[lst[end]] < start:
                new_length = (end - start) + 1
                print("new:{0}, start:{1}, end:{2}".format(new_length, start, end))
                if new_length > max_length:
                    max_length = new_length
            else:
                start = seen[lst[end]] + 1

        seen[lst[end]] = end
    return max_length


def test_substrings():
    ma = lengthOfLongestSubstring('abbbbcd')
    print(ma)


# test_substrings()


def threeSum(nums):
    ln = len(nums)
    if ln == 0:
        return []
    result = []
    seen = set()
    k = 3
    queue = collections.deque()
    queue.append((0, 1, nums[0]))
    while queue:
        start, end, total = queue.pop()
        if start == ln - 3:
            if end == k and total == 0:
                result([nums[start: start + end]])
            continue

        if end == k and total == 0:
            result.append([nums[start: start + end]])
            if start + end + 1 < ln:
                start = start + end + 1
                if start not in seen:
                    seen.add(start)
                    queue.appendleft((start, 1, nums[start]))
        else:
            if start + end < ln:
                queue.append((start, end + 1, total + nums[start + end]))
        if start+1 in seen:
            continue
        seen.add(start+1)
        if start + 1 < ln:
            queue.appendleft((start + 1, 1, nums[start + 1]))

    return result


def test_threeSum():
    num = threeSum([-1, 0, 1, 2, -1, -4])
    print(num)


#test_threeSum()

def nextPermutation(nums) :
    def swap_in_place(first, last):
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1

    ln = len(nums)
    if ln == 0:
        return
    swap_from = -1

    for i in range(ln - 1, -1, -1):
        if i - 1 > -1 and nums[i - 1] < nums[i]:
            swap_in = i - 1
            val = nums[i - 1]
            for j in range(i + 1, ln):
                if nums[j] > val:
                    swap_from = j
                    break
            if swap_from == -1:
                swap_from = i
            nums[swap_in], nums[swap_from] = nums[swap_from], nums[swap_in]
            swap_in_place(swap_in + 1, ln - 1)
            break
    else:
        nums = nums[::-1]
        print(nums)
def test_next_pen():
    val = [3,2,1]
    nextPermutation(val)
    print(val)
    val =val[::-1]
    print(val)

test_next_pen()