import sys

def intersect1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    results = []
    j = 0
    while j < len(nums2):
        for i in range(len(nums1)):
            if nums2[j] == nums1[i]:
                results.append(nums2[j])
                break
        j += 1

    return results


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    results = []
    j = 0
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    while j < len(nums2):
        for i in range(len(nums1)):
            if nums2[j] == nums1[i]:
                results.append(nums2[j])
                break
        j += 1

    return results


def test_intersect():
    result = intersect([1, 2, 2, 2, 1], [2, 2])
    print(result)
    result = intersect([1, 2, 2, 2, 1], [2, 2])
    print(result)


# test_intersect()

import collections

def findSubstring1(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """

    def permute(wds, memo):
        out = []
        if len(wds) == 1:
            return [wds[0]]
        search = ''.join(wds)
        if search in memo:
            return memo[search]
        else:
            for j, first in enumerate(wds):
                for perm in permute(wds[:j] + wds[j + 1:], memo):
                    out += [first + perm]
        memo[search] = out
        return out


    searches = permute(words, {})

    print(searches)
    len_search = len(searches[0])
    results = []
    if len_search == 1 and len(s) == 1:
        if s == searches[0]:
            return [0]

    for i in range(0, len(s) - len_search+1):
        sub = s[i:(i + len_search)]

        if sub in searches:
            results.append(i)

    return results

def findSubstring(s, words):
    if not s or not words:
        return []
    count = collections.Counter(words)
    wordLen = len(words[0])
    numWords = len(words)
    windowLen = wordLen * numWords
    res = []
    for i in range(len(s) - windowLen + 1):
        check = count.copy()
        for j in range(numWords):
            startIdx = i + j * wordLen
            word = s[startIdx: startIdx + wordLen]
            if word in check:
                check[word] -= 1
                if check[word] < 0:
                    break
            else:
                break
        if all([x == 0 for x in check.values()]):
            res.append(i)

    return res

def test_subString():
    result = findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(result)


    result = findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",
                           ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"])
    print(result)

    result = findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])
    print(result)



#test_subString()

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) == 0 or len(t) == 0:
        return ""

    counter = collections.Counter(t)
    lookup_counter = counter.copy()
    end = begin = 0
    t_len = len(t)
    match_len = len(s) + 1
    answer = ''
    while end < len(s):
        if s[end] in counter:
            counter[s[end]] -= 1
            if counter[s[end]] == 0:
                t_len -= lookup_counter[s[end]]
        end += 1
        while t_len == 0:
            if end - begin < match_len:
                match_len = end-begin
                answer = s[begin:end]

            if s[begin] in counter:
                counter[s[begin]] += 1
                if counter[s[begin]] > 0:
                    t_len += lookup_counter[s[begin]]
            begin += 1
    return answer

def minWindow2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) == 0 or len(t) == 0:
        return ""

    counter = collections.Counter(t)
    begin = end = 0
    search_length = len(t)
    min_string = ''
    min_length = len(s) + 1
    while end < len(s):
        if s[end] in counter:
            counter[s[end]] -= 1
            if counter[s[end]] == 0:
                search_length -= 1
        end += 1
        while search_length == 0:
            if end - begin < min_length:
                min_length = end - begin
                min_string = s[begin:end]
            if s[begin] in counter:
                counter[s[begin]] += 1
                if counter[s[begin]] > 0:
                    search_length += 1
            begin += 1
    return min_string
def test_sliding_window():
    result = minWindow("bba","ab")
    print(result)
    result = minWindow("aa","aa")
    print(result)
    result = minWindow("ADOBECODEBANC","ABC")
    print(result)

#test_sliding_window()

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 0 or k == 0:
        return []

    output = []
    queue = collections.deque()
    for i in range(0,len(nums)):
        queue.append(nums[i])
        if len(queue) == k:
            output.append(max(queue))
            queue.popleft()

    return output

def test_sliding():
    result = maxSlidingWindow([1,3,1,2,0,5],3)
    print(result)
    result = maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
    print(result)
    result = maxSlidingWindow([-7,-8,7,5,7,1,6,0],4)
    print(result)
#test_sliding()

def minCostII(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """

    def get_potential_house_colors(stk, house_no, previous_color, total_cost):
        if house_no >= len(costs):
            return

        for i in range(len(costs[house_no])):
            if i != previous_color:
                stk.append((house_no, i, costs[house_no][i] + total_cost))
    number_of_houses = len(costs)
    if number_of_houses == 0:
        return 0

    stack = collections.deque()
    get_potential_house_colors(stack, 0, -1, 0)
    min_cost = sys.maxsize
    while stack:
        item = stack.popleft()
        house_no, color_no, total_cost = item
        #print("house_no:{0}, color_no{1}, total_cost:{2}".format(house_no,color_no,total_cost))
        if house_no == number_of_houses - 1:
            if total_cost < min_cost:
                min_cost = total_cost
        else:
            get_potential_house_colors(stack, house_no+1, color_no, total_cost)
    return min_cost

def test_min_cost():
    result = minCostII([[1,5,3],[2,9,4]])
    print(result)
#test_min_cost()

def num_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = k
    diff = k * (k-1)
    for i in range(3, n+1):
        same, diff = diff , (same + diff) * (k-1)
    return same + diff

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[1]
    n = len(nums)
    dp = [0] * n
    dp[-1] = nums[n-1]
    dp[-2] = nums[n-2]
    for i in range(n-3, -1, -1):
        n_2 = i + 2
        n_3 = i + 3
        if n_2 <= n-1 and n_3 <= n-1:
            dp[i] += nums[i] + max(dp[n_2], dp[n_3])
        elif n_2 <= n-1:
            dp[i] += nums[i] + dp[n_2]

    return max(dp[0], dp[1])



def test_rob():
    num = rob([1,2,3,1])
    print(num)
    num = rob([2,7,9,3,1])
    print(num)
#test_rob()

def rob_2(nums):
    def max_money(numbers):
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        previous = 0
        current = 0
        for i in range(0, len(numbers)):
            previous, current = current, max(previous + numbers[i], current)
        return max(previous, current)
    max_money_1 = max_money(nums[:-1])
    max_money_2 = max_money(nums[1:])

    return max(max_money_1, max_money_2)


def test_rob2():
    num = rob_2([2,3,2])
    print(num)
    num = rob_2([1,2,3,1])
    print(num)

#test_rob2()

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    max_seq = 0
    running_seq = 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            running_seq += 1
        else:
            if max_seq < running_seq:
                max_seq = running_seq
            running_seq = 0
    if max_seq < running_seq:
        max_seq = running_seq

    return max_seq

def test_runningseq():
    num = findLengthOfLCIS([1334, 1500, 4169, 724, -3522, 4358, 1962, -536, 705, 3145, -1719, 1827, 4961, -4509, -2005, -3058, -173, 436, -2609, -396, -1098, -4847, -4708, -2618])
    print(num)
test_runningseq()