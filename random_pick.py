import collections
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_dict = collections.defaultdict(int)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        startAt = self.nums_dict[target]
        i = 0
        try:
            i = self.nums.index(target, startAt)

            self.nums_dict[target] = i+1
        except:
            print("reach here and i was {0}".format(i))
            i = self.nums.index(target, 0)
            self.nums_dict[target] = i+1

        return i


def test():
    s = Solution([1,2,3,2,3])

    print(s.pick(2))
    print(s.pick(2))
    print(s.pick(2))


a = 'abcded'
aa = list(a)
b = collections.Counter(a)
c = collections.defaultdict(int, aa)
c.clear()

print(c)