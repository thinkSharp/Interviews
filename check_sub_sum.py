def checkSubarraySum_recursive(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    goal: find the continuous subarray sum which is a multiple of of k and have at least size of 2
    plan:
        since we can have two decisions, either add another nother or drop one, I am taking recoursive approach.
        first_index, current_sum, next_index
    """
    ln = len(nums)

    def css(first_index, current_sum, next_index):
        print("f:{0}, s:{1},n:{2}".format(first_index, current_sum, next_index))
        if k != 0 and current_sum % k == 0:
            return True
        elif k == 0 and current_sum == k:
            return True
        elif next_index >= ln:
            return False
        ret = css(first_index, current_sum + nums[next_index], next_index + 1)
        ret |= css(first_index + 1, current_sum - nums[first_index]+ nums[next_index], next_index + 1)
        return ret

    if ln < 2:
        return False

    return css(0, nums[0] + nums[1], 2)


def test_checksum():
    result = checkSubarraySum_recursive([23,2,6,4,7], 0)
    print(result)

test_checksum()