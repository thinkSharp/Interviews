import math


def generatingPrime(num):
    def cross_off(local_prime):
        i = local_prime + local_prime
        while i < len(flags) - 1:
            flags[i] = False
            i += local_prime

    def get_next(local_prime):
        if local_prime >= len(flags):
            return 0
        while not flags[local_prime]:
            local_prime += 1
        return local_prime

    flags = [True] * (num + 1)
    prime = 2
    while prime <= math.sqrt(num):
        cross_off(prime)

        prime = get_next(prime+1)

    primes = [i for i in range(0, len(flags)-1) if flags[i] == True]
    return primes

def test_Prime():
    print(generatingPrime(50))
    print(generatingPrime(100))
    print(generatingPrime(10000))
    print(generatingPrime(100000))
    print(generatingPrime(1000000))

test_Prime()