import sys

'''
1. question: looking for shortest sub array accurance of short array in long, 
approach:
1. initialize array of same size as large for result
2. initialize array of same size as short for recording running value
3. loop from the back, in each iteration, see if that number belongs to short list, if it does then update the short_arry 
   with the index
4. calculate the closure, in order to calculate the closure, get the max of indexes excluding the max num
5. then calculate the diff from index and update the result array
6. after the loop return min value

time complexity => O(len(l) * len(s))
space complexity => O(len(l) + len(s))
iterate from the last index:
'''
def shortest_sequence(large, short):
    def get_closure(sr, index):
        val = max(sr)
        if val == sys.maxsize:
            return sys.maxsize
        else:
            return val - index

    result = [sys.maxsize] * len(large)
    short_with_max = [sys.maxsize] * len(short)

    for i in range(len(large) - 1, -1, -1):
        for j in range(0, len(short)):
            if large[i] == short[j]:
                short_with_max[j] = i
                result[i] = get_closure(short_with_max, i)
                continue
    return min(result)


def test_shortest_sequence():
    result = shortest_sequence([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], [1, 5, 9])
    print(result)
    assert(result == 3)

    result = shortest_sequence([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], [1, 5, 7,9])
    print(result)
    assert(result == 3)

test_shortest_sequence()
