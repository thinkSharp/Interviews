def operation(operator, num1, num2):
    def subtract(a,b):
        return a + negate(b)

    def multiply(a,b):
        abs_a = abs(a)
        abs_b = abs(b)
        if abs_a < abs_b:
            return multiply(b, a)
        mul_num = 0

        for i in range(abs_b, 0, -1):
            mul_num += a
        if b < 0:
            return negate(mul_num)
        return mul_num

    def divide(a,b):
        if b == 0:
            raise Exception('Divisible of zero exception')

        div_num = 0
        abs_a = abs(a)
        abs_b = abs(b)
        running_num = 0
        while running_num < abs_a:
            running_num += abs_b
            div_num +=1
        if (a < 0 and b < 0) or (a > 0 and b > 0):
            return div_num
        return negate(div_num)

    # we can improve by keep tracking the delta of all the sum(neg) until it is too big then reset to original
    # that will improve the performance and the time will O((log b)^2)
    def negate(b): # 0(b)
        num = -1 if b > 0 else 1
        neg = 0
        while b != 0:
            neg += num
            b += num
        return neg

    if operator == "+":
        return num1 + num2
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)


def test_operation():
    result = operation('+', 3, 5)
    print(result)
    result = operation('-', 3, 5)
    print(result)
    assert(result == -2)
    result = operation('-', -3, 5)
    print(result)
    assert(result == -8)
    result = operation('-', 3, -5)
    print(result)
    assert(result == 8)
    result = operation('*', 3, 5)
    print(result)
    assert(result == 15)
    result = operation('*', 3, -5)
    print(result)
    assert(result == -15)
    result = operation('*', -3, -5)
    print(result)
    assert(result == 15)
    result = operation('/', 15, 3)
    print(result)
    assert(result == 5)
    result = operation('/', -15, 3)
    print(result)
    assert (result == -5)
    result = operation('/', -15, -3)
    print(result)
    assert (result == 5)


test_operation()