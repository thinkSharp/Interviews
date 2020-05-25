# class Solution:
#     def add(self, num1: str, num2: str) -> str:
#         num1_rev, num2_rev = num1[::-1], num2[::-1]
#         n, m, carry = len(num1_rev), len(num2_rev), 0
#         result = ""
#         i = 0
#
#         while i < n or i < m or carry:
#             a = int(num1_rev[i]) if i < n else 0
#             b = int(num2_rev[i]) if i < m else 0
#             c = a + b + carry
#             sum_, carry = c % 10, c // 10
#             result += str(sum_)
#             i += 1
#         return result[::-1]
#
#     def multiply_by_single_digit(self, nums: str, x: str) -> str:
#         nums = nums[::-1]
#         carry, result = 0, ''
#         for y in nums:
#             z = (int(x) * int(y)) + carry
#             result += str(z % 10)
#             carry = z // 10
#         if carry > 0:
#             result += str(carry)
#         return result[::-1]
#
#     def multiply(self, num1: str, num2: str) -> str:
#         if not num1 or not num2:
#             return ''
#
#         placevalue = 0
#         result = '0'
#         for x in num2[::-1]:
#             row = self.multiply_by_single_digit(num1, x) + '0' * placevalue
#             placevalue += 1
#             result = self.add(result, row)
#         result = result.lstrip('0')
#         return result if result else '0'

class BigMultiply:
    def __init__(self):
        self.lookup = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}

    def add(self, num1, num2):
        carry = 0
        lst1 = list(num1)[::-1]
        lst2 = list(num2)[::-1]
        ln1 = len(lst1)
        ln2 = len(lst2)
        min_ln = min(ln1, ln2)
        result = []
        for i in range(min_ln):
            v1 = self.lookup[lst1[i]]
            v2 = self.lookup[lst2[i]]
            total = v1 + v2 + carry
            carry = 1 if total >= 10 else 0
            result.append(str(total)[-1])
        rest = lst1 if min_ln == ln2 else lst2
        for i in range(min_ln, len(rest)):
            val = self.lookup[rest[i]]
            total = val + carry
            carry = 1 if total >= 10 else 0
            result.append(str(total)[-1])
        if carry > 0:
            result.append(str(carry))
        return ''.join(result[::-1])

    def single_multiply(self, lst, s):
        carry = 0
        m = self.lookup[s]
        result = []
        for i in range(len(lst)):
            val = self.lookup[lst[i]]
            total = (val * m) + carry
            carry = total // 10
            digit = total % 10
            result.append(str(digit))
        if carry > 0:
            result.append(str(carry))
        return ''.join(result[::-1])
    def multiply(self, num1, num2):
        lst1 = list(num1)[::-1]
        lst2 = list(num2)[::-1]
        result = '0'
        zeros = 0
        for i in range(len(lst2)):
            val = self.single_multiply(lst1, lst2[i]) + ('0' * zeros)
            zeros += 1
            result = self.add(result, val)
        return result

def test_BigMultiply():
    bm = BigMultiply()
    res = bm.add("987", "55")
    print(res)
    res = bm.single_multiply('232141234', '5')
    print(res)
    res = bm.multiply("987","123")
    print(res)
#test_BigMultiply()


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    end = m + n - 1
    n = n - 1
    m -= 1
    while n >= 0 and m >= 0:
        if nums2[n] > nums1[m]:
            nums1[end] = nums2[n]
            n -= 1
        else:
            nums1[end], nums1[m] = nums1[m], nums1[end]
            m -= 1
        end -= 1

    while n >= 0:
        nums1[end] = nums2[n]
        n -= 1
        end -= 1

def test_merge():
    n1 = [1,3,5,0,0,0]
    n2 = [2,4,6]
    merge(n1,3, n2, 3)
    print(n1)

#test_merge()

def isOneEditDistance(s, t):
    one_edit, lns, lnt = 0, len(s), len(t)
    if 1 < abs(lns - lnt) > 1:
        return False
    i = 0
    j = 0
    while i < lns and j < lnt:
        if s[i] != t[j]:
            if one_edit == 0 and lns < lnt:
                one_edit = 1
                j += 1
            elif one_edit == 0 and lns == lnt:
                one_edit = 1
                i +=1
                j +=1
            elif one_edit == 0 and lns > lnt:
                one_edit = 1
                i += 1
            else:
                return False
        else:
            j += 1
            i += 1
    if i + 1 == lnt:
        one_edit += 1
    return True if one_edit == 1 else False

def test_one_edit():
    ret = isOneEditDistance('ad','abc')
    print(ret)
    ret = isOneEditDistance('a','')
    print(ret)
    ret = isOneEditDistance('','c')
    print(ret)
    ret = isOneEditDistance('','')
    print(ret)

#test_one_edit()
import re
def testIPs(ip):
    patternv4 = '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern_IPv4 = re.compile('^(' + patternv4 + r'\.){3}' + patternv4 + '$')
    patternv6 = '([0-9a-fA-F]{1,4})'
    pattern_IPv6 = re.compile('^(' + patternv6 + '\:){7}' + patternv6 + '$')

    if pattern_IPv4.match(ip):
        return 'IPv4'
    if pattern_IPv6.match(ip):
        return 'IPv6'
    else:
        return 'Neither'


def validPalindrome(s: str) -> bool:
    def is_palindrome(start, end, deleted):
        if start >= end:
            return True
        if s[start] != s[end] and deleted:
            return False
        if s[start] != s[end]:
            return is_palindrome(start + 1, end, True) or is_palindrome(start, end - 1, True)
        else:
            return is_palindrome(start + 1, end - 1, deleted)

    return is_palindrome(0, len(s) - 1, False)

def test_palindrome():
    test = validPalindrome('abcda')
    print(test)

test_palindrome()