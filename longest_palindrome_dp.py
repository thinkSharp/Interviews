def longest_palindrome(s):
    res, max_res, n = '', 0, len(s)
    if n == 0:
        return res
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
        res = s[i]
        max_res = 1
    print(dp)
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            res = s[i: i+2]
            max_res = 2
    print(dp)
    for i in range(n):
        for j in range(i-1):
            if s[i] == s[j] and dp[j+1][i-1]:
                dp[j][i] = 1
                if i-j+1 > max_res:
                    max_res = i-j+1
                    res = s[j: i+1]
    return res

def test_longest_palindrome():
    num = longest_palindrome('bbabad')
    print(num)

#test_longest_palindrome()

def numDecodings(s):
    if not s:
        return 0
    ln = len(s)
    dp = [0 for _ in range(ln+1)]
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, ln+1):
        dp[i] += dp[i-1]
        two_digit = int(s[i-2: i])
        if two_digit >= 10 and two_digit <= 26:
            dp[i] += dp[i-2]
    return dp[ln]

def numDecodings2(s):
    def rec_decode(index, ln):
        if index == ln:
            return 1

        if s[index] == '0':
            return 0

        if index == ln - 1:
            return 1

        if index in memo:
            return memo[index]

        ans = rec_decode(index+1, ln)
        ans += rec_decode(index+2, ln) if int(s[index:index+2]) <= 26 else 0

        memo[index] = ans

        return ans

    l = len(s)
    if l == 0:
        return 0
    memo = {}
    return rec_decode(0, l)



def test_decoding():
    num = numDecodings('2126')
    print(num)
    num = numDecodings2('2126')
    print(num)
#test_decoding()

import collections
collections.de
def longestValidParentheses(s):
    stack = collections.deque()
    n, count = len(s), 0
    if n == 0:
        return 0
    stack.append(-1)
    for i, w in enumerate(s):
        if w == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                count = max(count, i - stack[-1])
    return count

def wordBreak(s, wordDict):
    ln = len(s)
    if ln == 0:
        return False

    queue = collections.deque()
    visited = set()
    queue.append((0, []))
    result = []
    while queue:
        print(queue)
        start, res = queue.pop()

        if start == ln:
            result.append(res)
            # return True

        #if start in visited:
            #continue

        visited.add(start)

        for end in range(start + 1, ln + 1):
            if s[start:end] in wordDict:
                queue.appendleft((end, res + [s[start:end]]))

    print(result)
    return len(result) != 0

def test_word_break():
    num = wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"])
    print(num)

test_word_break()

''''
private int[][] dp;

public NumMatrix(int[][] matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) return;
    dp = new int[matrix.length][matrix[0].length + 1];
    for (int r = 0; r < matrix.length; r++) {
        for (int c = 0; c < matrix[0].length; c++) {
            dp[r][c + 1] = dp[r][c] + matrix[r][c];
        }
    }
}

public int sumRegion(int row1, int col1, int row2, int col2) {
    int sum = 0;
    for (int row = row1; row <= row2; row++) {
        sum += dp[row][col2 + 1] - dp[row][col1];
    }
    return sum;
}

'''