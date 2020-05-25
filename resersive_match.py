def isMatch2(text, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]


def isMatch(text, pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

def isMatch_2(s, p):
    if not p:
        return not s
    memo = {}
    len_s = len(s)
    len_p = len(p)

    def dp(i, j):
        if (i, j) not in memo:
            if j == len_p:
                ans = i == len_s
            else:
                first_case = i < len_s and p[j] in {s[i], '.'}
                if j + 1 < len_p and p[j + 1] == '*':
                    ans = dp(i, j + 2) or first_case and dp(i + 1, j)
                else:
                    ans = first_case and dp(i + 1, j + 1)
            memo[(i, j)] = ans
        return memo[(i, j)]

    return dp(0, 0)
def isMatch2(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


def test_isMatch():
    result = isMatch('aa','a*')
    print(result)
    result = isMatch('aabcdefg','a.*')
    print(result)

#test_isMatch()

def wild_card(s,p):
    if not p:
        return not s
    len_s = len(s)
    len_p = len(p)
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if j == len_p:
                ans = i == len_s
            elif i == len_s and p[j] == '*' and j == len_p - 1:
                ans = True
            elif i >= len_s and j != len_p:
                ans = False
            else:

                first = i < len_s and p[j] in {s[i], '?', '*'}
                #print("first:{0}, p:{1}, s:{2}".format(first, p[j], s[i]))
                if p[j] == '*':
                    ans = dp(i, j + 1) or first and dp(i + 1, j)
                else:
                    ans = first and dp(i + 1, j + 1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

def test_wild_card():
    result = wild_card('acdcb',"a*c?b")
    print(result)
    result = wild_card('abbbbbbbba', "?*a")
    print(result)
    result = wild_card('abbbbbbbba', "?*")
    print(result)
#test_wild_card()

