def countSmaller(nums):
    result, arr = [], []
    for num in nums[::-1]:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == num and ((mid and arr[mid - 1] != arr[mid]) or not mid):
                l = mid
                break
            elif arr[mid] < num:
                l = mid + 1
            else:
                r = mid
        arr.insert(l, num)
        result.append(l)
    return result[::-1]

def count_all_smaller(nums):
    def build_bst(bst, item):
        left, right = 0, len(bst)
        while left < right:
            mid = (left + right) // 2
            if bst[mid] == item and ((mid and bst[mid-1] != bst[mid]) or not mid):
                left = mid
                break
            elif bst[mid] < item:
                left = mid + 1
            else:
                right = mid
        bst.insert(left,item)
        return left

    if len(nums) == 0:
        return nums
    results = [0] * len(nums)
    bst_arr = []
    for i in range(len(nums)-1, -1, -1):
        count = build_bst(bst_arr, nums[i])
        results[i] = count
    print(bst_arr)
    return results

def test_count_all_smaller():
    results = count_all_smaller([5,2,6,6,6,1])
    print(results)
#test_count_all_smaller()

import collections

od = collections.OrderedDict()
od[1] = 1
od[2] = 2
od[3] = 97
od[4] = 4
od[5] = 5
del od[1]
od[1] = 6
print(od)
print(len(od))
od.popitem(last=False)
print(od)
_,del_index = od.popitem(last=False)
print(del_index)

item = od.pop(3)
print(item)

od.pop
