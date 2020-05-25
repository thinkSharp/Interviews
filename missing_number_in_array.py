import math

def missing_number(lst, n):
    x_or = 0
    for i in lst:
        x_or = x_or ^ i
    for i in range(0, n+1):
        x_or = x_or ^ i
    return x_or


def solve_quadratic(lst, n):
    def sum_square():
        sum_sqr = 0
        for i in range(1,n+1):
            sum_sqr += (i*i)
        return sum_sqr

    def sum_square_lst():
        sum_sqr = 0
        for i in lst:
            sum_sqr += (i*i)
        return sum_sqr

    def number_sum():
        num_sum = 0
        for i in range(1, n + 1):
            num_sum += i
        return num_sum

    def number_sum_lst():
        sum_num = 0
        for i in lst:
            sum_num += i
        return sum_num

    diff_square = sum_square() - sum_square_lst()
    diff_sum = number_sum() - number_sum_lst()

    '''
    x + y = s
    x^2 + y^2 = t
    y = s - x
    x^2 + (s - x)^2 = t
    x^2 + x^2 -2sx + s^2 - t = 0
    2x^2 -2sx + s^2-t = 0
    x = -b +- sqrt(b^2 -4ac) / 2a
    a = 2
    b = -2*s
    c = s^2-t
    '''
    a = 2
    b = -2* diff_sum
    c = (diff_sum*diff_sum) - diff_square
    p1 = b * b
    p2 = 4 * a * c

    bb = p1 - p2
    a2 = 2 * a
    minus_b = -1 * b
    d = math.sqrt(bb)

    x = int((minus_b + d) / a2)
    y = diff_sum - x

    return x, y

print(solve_quadratic([1,2,3,6,5], 7))
print(missing_number([1,2,3,5], 5))
print(missing_number([1,3,5,6], 7))

print((1.5+2)/2)
print((1.5+2+2)/3)