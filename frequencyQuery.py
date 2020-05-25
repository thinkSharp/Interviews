def freqQuery(queries):
    items = {}
    frequency = {}
    result = []
    count = 0

    for action, item in queries:
        if action == 1:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
            last_freq = items[item] - 1
            if last_freq in frequency:
                if item in frequency[last_freq]:
                    frequency[last_freq].remove(item)
                if not frequency[last_freq]:
                    del frequency[last_freq]
            current_freq = items[item]
            if current_freq in frequency:
                frequency[current_freq].append(item)
            else:
                frequency[current_freq] = [item]
        elif action == 2:
            if item in items:
                last_freq = items[item]
                items[item] -=1
                current_freq = items[item]
                if current_freq == 0:
                    del items[item]
                if last_freq in frequency:
                    if item in frequency[last_freq]:
                        frequency[last_freq].remove(item)
                    if not frequency[last_freq]:
                        del frequency[last_freq]
                if current_freq in frequency:
                    frequency[current_freq].append(item)
                else:
                    frequency[current_freq] = [item]
        elif action == 3:
            if item in frequency and len(frequency[item]) > 0:
                result.append(1)
            else:
                result.append(0)
    return result



def test():
    result = freqQuery([(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)])
    print(result)
    result = freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)])
    print(result)
    assert (result == [0, 1])
    result = freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)])
    print(result)
    assert (result == [0, 1])
    result = freqQuery([(3, 4), (2, 1003), (1, 16), (3, 1)])
    print(result)
    assert (result == [0, 1])


test()

#test2()

#result = freqQuery([(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)])
#print(result)
