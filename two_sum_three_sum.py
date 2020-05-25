# time complexity O of (n)
# space complexity 0 of (n)
def two_sum(nums, target):
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    map_nums = {}
    for i in range(len_nums):
        remainder = target - nums[i]
        if remainder in map_nums:
            return [map_nums[remainder], i]
        map_nums[nums[i]] = i
    return []


def two_sum_for_sorted(nums, target):
    low = 0
    high = len(nums) -1
    while low < high:
        sum_nums = nums[low] + nums[high]
        if target == sum_nums:
            return [low, high]
        elif sum_nums < target:
            low += 1
        else:
            high -= 1
    return []

def three_sum(nums):
    def two_sum_sorted(skip_index, results):
        low = skip_index + 1
        high = len(nums) - 1
        while low < high:
            sum_nums = nums[skip_index] + nums[low] + nums[high]
            if sum_nums < 0 or (low > skip_index + 1 and nums[low] == nums[low-1]):
                low += 1
            elif sum_nums > 0 or (high < len(nums)-1 and nums[high] == nums[high+1]):
                high -= 1
            else:
                results.append([nums[skip_index], nums[low], nums[high]])
                low += 1
                high -= 1

    len_nums = len(nums)
    if len_nums == 0:
        return []
    results = []
    nums = sorted(nums)
    for i in range(len_nums):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        two_sum_sorted(i, results)

    return results

def test_three_sum():
    result = three_sum([-1,0,1,2,-1,-4])
    print(result)

test_three_sum()

def test_two_sum():
    result = two_sum([2,7,11,15], 9)
    print(result)
    result = two_sum([2, 7, 11, 15], 13)
    print(result)
    result = two_sum([2, 7, 11, 15], 18)
    print(result)
    result = two_sum([2, 7, 11, 15], 17)
    print(result)
    result = two_sum([2, 7, 11, 15], 22)
    print(result)
    result = two_sum_for_sorted([2,7,11,15], 9)
    print(result)
    result = two_sum_for_sorted([2, 7, 11, 15], 13)
    print(result)
    result = two_sum_for_sorted([2, 7, 11, 15], 18)
    print(result)
    result = two_sum_for_sorted([2, 7, 11, 15], 17)
    print(result)
    result = two_sum_for_sorted([2, 7, 11, 15], 22)
    print(result)
#test_two_sum()



