'''
DP problem similar to Buy and Sell Stock
H0[i] means the max sum at nums[i] when the first index is choosen.
H1[i] means the max sum at nums[i] when the second index is choosen.
H2[i] means the max sum at nums[i] when the third index is choosen.
Build a prefixSum array, PreSum[i] = sum(nums[:i])
H0[i] = max(H0[i-1], PreSum[i+k]-PreSum[i])
H1[i] = max(H1[i-1], H0[i-k]+PreSum[i+k]-PreSum[i])
H2[i] = max(H2[i-1], H1[i-k]+PreSum[i+k]-PreSum[i])
For H0, iterate i from 0 to len(nums)-k
For H1, iterate i from k to len(nums)-k
For H2, iterate i from 2*k to len(nums)-k
Track the index of each choice.
Time: O(n)
Space: O(n)
'''
def maxSumOfThreeSubarrays_org(nums, k):
    len_nums = len(nums)
    PreSum = [0]
    for n in nums:
        PreSum += [n + PreSum[-1]]


    H0, H1, H2 = [-1] * len_nums, [-1] * len_nums, [-1] * len_nums
    idx0, idx1, idx2 = [None] * len_nums, [None] * len_nums, [None] * len_nums
    for i in range(len_nums - k + 1):
        add = PreSum[i + k] - PreSum[i]
        H0[i] = add
        idx0[i] = [i]
        if i > 0 and H0[i - 1] >= H0[i]:
            H0[i] = H0[i - 1]
            idx0[i] = idx0[i - 1]
        if i >= k:
            H1[i] = H0[i - k] + add
            idx1[i] = idx0[i - k] + [i]
            if i > k and H1[i - 1] >= H1[i]:
                H1[i] = H1[i - 1]
                idx1[i] = idx1[i - 1]
        if i >= 2 * k:
            H2[i] = H1[i - k] + add
            idx2[i] = idx1[i - k] + [i]
            if i > 2 * k and H2[i - 1] >= H2[i]:
                H2[i] = H2[i - 1]
                idx2[i] = idx2[i - 1]

    return idx2[len_nums - k]

def maxSumOfThreeSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    goal: get the maximum sum of 3 non-over lapping sub array
    appraoch:
        solve via dp approach
        first calculate all the sum till index
        since the application is asking for 3 non overlapping sub sums
        the steps in the loops are performs 3 times if valid
        seond in the loop starting index 0 to ln-k+1, get the sums of k elements
            first calculate the sum of k element
            add in the sub1[i] index, sub_index1[i] the index of starting k
            check if sub1[i-1] sum is greater or equal, if it is then copy them to i position

            for second do the same thing if i >= k

            for third do the same thing if i >= 2k

            at the end the result will be stored in sub_index2[ln - k] position
    """
    ln = len(nums)
    if ln == 0 or k == 0:
        return []

    sums = [0] * (ln + 1)
    i = 1
    for n in nums:
        sums[i] = sums[i - 1] + n
        i += 1
    print(sums)
    sub1, sub2, sub3 = [0] * ln, [0] * ln, [0] * ln
    sub1_idx, sub2_idx, sub3_idx = [0] * ln, [0] * ln, [0] * ln

    for i in range(ln - k + 1):
        val_3_sum = sums[i + k] - sums[i]

        sub1[i] = val_3_sum
        sub1_idx[i] = [i]
        if i > 0 and sub1[i - 1] >= sub1[i]:
            sub1[i] = sub1[i - 1]
            sub1_idx[i] = sub1_idx[i - 1]

        if i >= k:
            sub2[i] = sub1[i-k] + val_3_sum
            sub2_idx[i] = sub1_idx[i-k] + [i]
            if i > k and sub2[i - 1] >= sub2[i]:
                sub2[i] = sub2[i - 1]
                sub2_idx[i] = sub2_idx[i - 1]

        if i >= 2 * k:
            sub3[i] = sub2[i-k] + val_3_sum
            sub3_idx[i] = sub2_idx[i-k] + [i]
            if i > 2 * k and sub3[i - 1] >= sub3[i]:
                sub3[i] = sub3[i - 1]
                sub3_idx[i] = sub3_idx[i - 1]

    return sub3_idx[ln - k]
def test_max_sum():
    result = maxSumOfThreeSubarrays_org([1,2,1,2,6,7,5,1], 2)
    print (result)
    result = maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
    print (result)

test_max_sum()