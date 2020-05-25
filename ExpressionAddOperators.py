def addOperators(num, target):
    N = len(num)
    answers = []

    def recurse(index, prev_operand, current_operand, value, string):

        # Done processing all the digits in num
        if index == N:

            # If the final value == target expected AND
            # no operand is left unprocessed
            if value == target and current_operand == 0:
                answers.append("".join(string[1:]))
            return

        # Extending the current operand by one digit
        current_operand = current_operand * 10 + int(num[index])
        str_op = str(current_operand)

        # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
        # valid operand. Hence this check
        if current_operand > 0:
            # NO OP recursion
            recurse(index + 1, prev_operand, current_operand, value, string)

        # ADDITION
        string.append('+');
        string.append(str_op)
        recurse(index + 1, current_operand, 0, value + current_operand, string)
        string.pop();
        string.pop()

        # Can subtract or multiply only if there are some previous operands
        if string:
            # SUBTRACTION
            string.append('-');
            string.append(str_op)
            recurse(index + 1, -current_operand, 0, value - current_operand, string)
            string.pop();
            string.pop()

            # MULTIPLICATION
            string.append('*');
            string.append(str_op)
            recurse(index + 1, current_operand * prev_operand, 0,
                    value - prev_operand + (current_operand * prev_operand), string)
            string.pop();
            string.pop()

    recurse(0, 0, 0, 0, [])
    return answers

def test_op():
    result = addOperators("123", 6)
    print(result)

test_op()