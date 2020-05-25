def TripleStep(stairs):
    def countWays(step, cache):
        if step < 0:
            return 0
        elif step == 0:
            return 1
        elif cache[step] > 0:
            return cache[step]
        else:
            cache[step] = countWays(step-1, cache) + countWays(step-2, cache) + countWays(stairs-3, cache)
        return cache[step]

    memo = [0] * (stairs + 1)
    return countWays(stairs, memo)



def test_tripleStep():
    print(TripleStep(4))


test_tripleStep()
