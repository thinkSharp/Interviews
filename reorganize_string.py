import collections
import heapq

def reorganize_string(st):
    ln = len(st)
    counter = collections.Counter(st)
    heap = []
    for k, v in counter.items():
        heap.append((-v, k))

    heapq.heapify(heap)

    res = []
    while len(heap) > 1:
        count1, c1 = heapq.heappop(heap)
        count2, c2 = heapq.heappop(heap)

        res.extend([c1, c2])
        if count1 + 1:
            heapq.heappush(heap, (count1+1, c1))
        if count2 + 1:
            heapq.heappush(heap, (count2+1, c2))

    if len(heap) > 0:
        count, c = heapq.heappop(heap)
        if count < -1:
            return ""

        res.append(c)

    return ''.join(res)


def test_reorganize_string():
    res = reorganize_string('aabbaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    print(res)
    res = reorganize_string('aabbbaacc')
    print(res)
    res = reorganize_string('aab')
    print(res)
test_reorganize_string()
