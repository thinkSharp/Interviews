import collections


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    goal: return all possible sentences from the string by looking up dictionary
    steps:
        going to use breath first search
        build all possible paths
        return paths
    """

    def word_break_recursive(str_len, index):
        if index in paths:
            return paths[index]

        local_list = []
        if index == str_len:
            local_list.append([])

        for end in range(index + 1, str_len + 1):
            if s[index: end] in wordDict:
                paths_from_index = word_break_recursive(str_len, end)
                for p in paths_from_index:
                    local_p = []
                    for item in p:
                        local_p.append(item)
                    local_p.append(s[index:end])
                    local_list.append(local_p)

        paths[index] = local_list
        return local_list

    str_s = len(s)
    paths = {}
    val = word_break_recursive(str_s, 0)
    result = []
    print(paths)
    for lst in val:
        str_l = ' '.join(lst)
        result.append(str_l)

    return result






def test_word_break():
    result = wordBreak("catsanddog",["cat","cats","and","sand","dog"])
    print(result)
    #result = wordBreak('leetcode',set(['leet','code', 'l','eetc','ode']))
    #print(result)

#test_word_break()

stack = collections.deque()

print(stack is None)
stack.append(3)
print(len(stack) == 0)
