def rotLeft(a, b):
    if b == 0:
        return a

    lst = [0] * len(a)
    new_index = 0
    for i in range(b, len(a)):
        new_index = i -b
        lst[new_index] = a[i]
    new_index += 1
    for i in range(0, b):
        lst[new_index + i] = a[i]
    return lst

print(rotLeft([1,2,3,4,5], 2))
print(rotLeft([1,2,3,4,5], 4))

import math
print(math.log(81,3))