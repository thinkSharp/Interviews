def calculator(expression):
    def calc(op, v1, v2):
        if op == '+':
            return v1 + v2
        elif op == '-':
            return v1 - v2
        elif op == '*':
            return v1 * v2
        elif op == '/':
            return v1 / v2
        return 0

    def getValue(j):
        temp = ''
        while j < len_exp:
            temp += expression[j]
            j += 1
            if j < len_exp:
                if expression[j] in operators:
                    break
        return float(temp), j

    len_exp = len(expression)
    if len_exp == 0:
        return 0
    if len_exp == 1:
        return expression[0]

    operators = ['+', '-', '*', '/']
    next_val = 0
    result, i = getValue(0)
    current_op = ''
    while i < len_exp:
        if expression[i] in operators:
            if current_op == '':
                current_op = expression[i]
                i += 1
                continue
            else:
                next_op = expression[i]
                if next_op == '+' or next_op == '-':
                    before = result
                    result = calc(current_op, result, next_val)
                    print("1. result: {0}, op: {1}, {2} {3}".format(result, current_op, before, next_val))
                    current_op = next_op
                    i += 1
                else:
                    if i + 1 < len_exp:
                        temp_val, i = getValue(i + 1)
                        before = next_val
                        next_val = calc(next_op, next_val, temp_val)
                        print("2. result: {0}, op: {1}, {2} {3}".format(next_val, next_op, before, temp_val))
                    else:
                        return 0

        else:
            next_val, i = getValue(i)
    before = result
    result = calc(current_op, result, next_val)
    print("3. result: {0}, op: {1}, {2} {3}".format(result, current_op, before, next_val))
    return result


def test_calculator():
    result = calculator('2*3+5/6*3+15')
    print(result)
    assert(result == 23.5)
    result = calculator('15+143')
    print(result)
    assert(result == 158)
    result = calculator('15/3+4*5')
    print(result)
    assert(result == 25)


#test_calculator()

def divide(dividend, divisor):

    max_div_num = pow(2,30)

    negative = 2
    if dividend < 0:
        negative -= 1
        dividend = -dividend
    if divisor < 0:
        negative -= 1
        divisor = -divisor

    if divisor == 1:
        return -dividend if negative == 1 else dividend

    doubles = []
    power = []
    divide_count = 1
    while divisor <= dividend:
        doubles.append(divisor)
        power.append(divide_count)

        if divisor > max_div_num:
            break

        divisor += divisor
        divide_count += divide_count
    quotient = 0
    for i in range(len(doubles)-1, -1, -1):
        divisor = doubles[i]
        power_of_two = power[i]
        if divisor <= dividend:
            dividend -= divisor
            quotient += power_of_two

    return -quotient if negative == 1 else quotient

def test_divide():
    result = divide(100, 3)
    print(result)
    result = divide(1, 3)
    print(result)
    result = divide(-1000000000000, 3)
    print(result)
    result = divide(-100, -3)
    print(result)
    result = divide(10, -3)
    print(result)

test_divide()