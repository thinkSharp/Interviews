import sys

def zero_count_in_factorial(n):
    count = 0
    i = 5
    while i <= n:
        count += n//i
        i *=5
    return count

def test_zero_count():
    print(zero_count_in_factorial(5))
    print(zero_count_in_factorial(10))
    print(zero_count_in_factorial(30))

test_zero_count()

##############################################################################

def smallest_difference(a,b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)
    min_val = sys.maxsize
    while i < len_a and j < len_b:
        diff = abs(sorted_a[i] - sorted_b[i])
        if min_val > diff:
            min_val = diff
        if sorted_a[i] < sorted_b[j]:
            i += 1
        else:
            j += 1

    return min_val


def test_smallest_diff():
    result = smallest_difference([1,2,11,15], [4,12,19,23,127,235])
    print(result)

#test_smallest_diff()

def flip(a):
    return 1^a

def sign(a):
    return flip(a >> 31) & 0x01

def max_num(a,b):
    k = sign(a-b)
    q = flip(k)
    return a * k + b * q

print(max_num(2,3))
print(max_num(5,4))
print(max_num(5,5))


def convert_string_to_number(num):
    def converter_for_hundreds(small_num):
        str_hundred = ''
        in_hundred = small_num // 100
        if in_hundred > 0:
            str_hundred += num_dict[in_hundred] + ' ' + num_dict[100]
            small_num %= 100

        while small_num > 0:
            for d in small:
                result = small_num // d
                small_num %= d
                if result > 0:
                    if len(str_hundred) > 0:
                        str_hundred += ' '
                    str_hundred += num_dict[d]
        return str_hundred

    num_dict = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
                11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
                18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty',
                70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred', 1000:'Thousand', 1000000:'Million',
                1000000000:'Billion'}
    divisor = [1000000000, 1000000, 1000]
    small = [90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,10,9,8,7,6,5,4,3,2,1]
    str_num = ''
    if num == 0:
        return 'Zero'

    while num > 0:
        for div in divisor:
            res = num // div
            num = num % div

            if res > 0:
                str_small = converter_for_hundreds(res)
                if len(str_num) > 0:
                    str_num += ' '
                str_num += str_small + ' ' + num_dict[div]

        str_remaining = converter_for_hundreds(num)
        if len(str_remaining) > 0:
            if len(str_num) > 0:
                str_num += ' '
            str_num += str_remaining
        num = 0
    return str_num


def test_convert():
    result = convert_string_to_number(0)
    print(result)

    result = convert_string_to_number(120)
    print(result)

    result = convert_string_to_number(83)
    print(result)

    result = convert_string_to_number(12)
    print(result)

    result = convert_string_to_number(5)
    print(result)

    result = convert_string_to_number(1200)
    print(result)

    result = convert_string_to_number(45120)
    print(result)

    result = convert_string_to_number(152120)
    print(result)

    result = convert_string_to_number(1345120)
    print(result)

    result = convert_string_to_number(13543243171)
    print(result)


test_convert()