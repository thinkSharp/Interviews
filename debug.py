import collections

import heapq

class Interval:
    def __init__(self, start=0, end=0):
        self.start = start,
        self.end = end

def employeeFreeTime(avails):
    ans = []
    pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
    heapq.heapify(pq)
    anchor = min(iv.start for emp in avails for iv in emp)
    while pq:
        t, e_id, e_jx = heapq.heappop(pq)
        if anchor < t:
            ans.append(Interval(anchor, t))
        a = avails[e_id][e_jx]
        anchor = max(anchor, avails[e_id][e_jx].end)
        if e_jx + 1 < len(avails[e_id]):
            heapq.heappush(pq, (avails[e_id][e_jx + 1].start, e_id, e_jx + 1))

    return ans

def test_removeDup():
    res = employeeFreeTime([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])
    print(res)

test_removeDup()
