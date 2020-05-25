import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k= 200):
        res = []
        h = []
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return res
        i = 0
        while i < len(nums1) and i < k:
            heapq.heappush(h, (nums1[i] + nums2[0], nums1[i], 0))
            i += 1
        while k and h:
            s, a1, ln = heapq.heappop(h)
            res.append(s)
            if ln == len(nums2) - 1:
                continue
            heapq.heappush(h, (a1 + nums2[ln + 1], a1, ln + 1))
            print(res)
            print(h)
            k -= 1
        return res

    def kthSmallest(self, mat, k):
        m, n = len(mat), len(mat[0])
        res = mat[0]
        for i in range(1, m):
            res = self.kSmallestPairs(res, mat[i])
        return res[k - 1]

def kthSmallest(mat, k):
    def two_sums(a1, a2, l1, l2, k):
        k = min(l1*l2, k)
        ans, seen, heap = [], set(), [(a1[0] + a2[0], 0, 0)]
        while k:
            s, cla, clb = heapq.heappop(heap)

            ans.append(s)
            k -= 1

            if cla + 1 < l1 and (cla + 1, clb) not in seen:
                seen.add((cla + 1, clb))
                heapq.heappush(heap, (a1[cla + 1] + a2[clb], cla + 1, clb))
            if clb + 1 < l2 and (cla, clb + 1) not in seen:
                seen.add((cla, clb + 1))
                heapq.heappush(heap, (a1[cla] + a2[clb + 1], cla, clb + 1))
            print(heap)
            print(ans)
        return ans

    m = len(mat)
    if k == 0 or m == 0:
        return 0
    n = len(mat[0])
    res = mat[0]
    for i in range(1, m):
        res = two_sums(res, mat[i], m, n, k)
    return res[-1]


def k_smallest_sum2(mat, k):
    def two_array_add(a1, a2, l1, l2, k):
        k = min(l1 * l2, k)
        ans, seen, heap = [], set(), [(a1[0] + a2[0], 0, 0)]
        heapq.heapify(heap)
        while k:
            s, i1, i2 = heapq.heappop(heap)
            ans.append(s)
            k -= 1

            if i1 +1 < l1 and (i1 + 1, i2) not in seen:
                seen.add((i1+1, i2))
                heapq.heappush(heap, (a1[i1+1] + a2[i2], i1+1, i2))
            if i2 +1 < l2 and (i1, i2 + 1) not in seen:
                seen.add((i1, i2+1))
                heapq.heappush(heap, (a1[i1] + a2[i2 +1], i1, i2 + 1))
            print(heap)
            print(ans)
        return ans

    m, n = len(mat), len(mat[0])
    arr1 = mat[0]
    for row in range(1, m):
        arr1 = two_array_add(arr1, mat[row], len(arr1), n, k)
    return arr1[-1]

def kthSmallest2(mat, k):

    def TwoArray(arr1, arr2, n1, n2, k):
        k = min(k, n1 * n2)
        ans, seen, h = [], set(), [(arr1[0] + arr2[0], 0, 0)]
        #heapq.heapify(h)
        while k:
            s, i1, i2 = heapq.heappop(h)
            ans.append(s)
            k -= 1
            if i1 + 1 < n1 and (i1 + 1, i2) not in seen:
                seen.add((i1 + 1, i2))
                heapq.heappush(h, (arr1[i1 + 1] + arr2[i2], i1 + 1, i2))
            if i2 + 1 < n2 and (i1, i2 + 1) not in seen:
                seen.add((i1, i2 + 1))
                heapq.heappush(h, (arr1[i1] + arr2[i2 + 1], i1, i2 + 1))
            print(h)
            print(ans)
        return ans

    m, n = len(mat), len(mat[0])
    arr1 = mat[0]
    for row in range(1, m):
        arr1 = TwoArray(arr1, mat[row], len(arr1), n, k)
    return arr1[-1]

def test_k_smallest():
    ret = kthSmallest([[1,3,11],[2,4,6]], 9)
    print(ret)
    ret = kthSmallest2([[1,3,11],[2,4,6]], 9)
    print(ret)
    #sol = Solution()
    #ret = sol.kthSmallest([[1,3,11],[6,4,2]], 5)
    #print(ret)
test_k_smallest()
