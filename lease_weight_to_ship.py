def shipWithinDays(weights, D):
    def is_possible(capacity, w, d):
        remaining = capacity
        count = 1
        for item in w:
            if item > capacity:
                return False
            elif item > remaining:
                count += 1
                remaining = capacity
            remaining -= item
        return count <= d

    if D == 0:
        return 0
    if D == 1:
        return sum(weights)
    low = 0
    high = max(weights) * len(weights) // D + 1
    while low <= high:
        mid = (low + high) // 2
        if not is_possible(mid, weights, D):
            low = mid + 1
        else:
            high = mid - 1
    return low

def test_shipWithinDays():
    weight = shipWithinDays([3,2,2,4,1,4], 3)
    print(weight)
    weight = shipWithinDays([1,2,3,1,1], 4)
    print(weight)

test_shipWithinDays()