import sys
##
# main idea for having two eggs and n floors
# if a floor is picked and throw the eggs, there are two possibilities, either the egg will break or not
# therefore, we need to calculate possibilities for both so for j = 2 and i = 2 (eggs)
# if we throw egg from 2nd floor,
# 1 + max( (firstfloor, egg droop), (rest, one less egg))
# 1 + max( (firstfloor, egg drop),
##
def minimumEggDrop(floor, eggs):
    floor = floor + 1
    eggs = eggs + 1
    result = [[0] * floor for i in range(0, eggs)]

    for i in range(1,eggs):
        result[i][1] = 1
    for i in range(1, floor):
        result[1][i] = i

    for i in range(2, eggs):
        for j in range(2, floor):
            result[i][j] = sys.maxsize
            for k in range(1,j):
                c = 1 + max(result[i-1][k-1], result[i][j-k])
                if c < result[i][j]:
                    result[i][j] = c

    print(result)


minimumEggDrop(10, 2)

