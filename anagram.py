import collections
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    goal: find all anagrams in the string
    steps:
        1) create a counter of p to know exactly how many letters and their count
        2) add p in dictionary for quick look up
        3) have a distinct count to store the actual count of letters
        4) look through s and along the way keep track of distinct count and running count of all the p letters , and potential start of new anagrams
        5) save all the findings in list
    """

    len_s, len_p = len(s), len(p)

    if len_s == 0 or len_p == 0 or len_s < len_p:
        return []

    result = []
    p_counter = collections.Counter(p)
    s_counter = collections.Counter()

    for i in range(len_s):
        s_counter[s[i]] += 1

        if i >= len_p:
            if s_counter[s[i-len_p]] == 1:
                del s_counter[s[i-len_p]]
            else:
                s_counter[s[i-len_p]] -= 1

        if p_counter == s_counter:
            result.append(i-len_p + 1)

    return result

def test_anagram():
    result = findAnagrams("cbaebabacd","abc")
    print(result)
    result = findAnagrams("ccbabcebabbaaacbad","abac")
    print(result)

test_anagram()