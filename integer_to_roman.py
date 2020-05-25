def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    def roman_after(after_num, div):
        after_result = []
        while after_num >= div:
            res_after = after_num // div
            after_num -= div
            if res_after > 0:
                after_result.append(num_to_symbol[div])
        return after_num, after_result

    if 1 > num > 3999:
        return num

    num_to_symbol = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    result = []

    while num > 0:
        if num >= 1000:
            num, res = roman_after(num, 1000)
            result += res
        elif num >= 900:
            result.append('CM')
            num -= 900
        elif num >= 500:
            result.append('D')
            num -= 500
            num, res = roman_after(num, 100)
            result += res
        elif num >= 400:
            result.append('CD')
            num -= 400
        elif num >= 100:
            num, res = roman_after(num, 100)
            result += res
        elif num >= 90:
            result.append('XC')
            num -= 90
        elif num >= 50:
            result.append('L')
            num -= 50
            num, res = roman_after(num, 10)
            result += res
        elif num >= 40:
            result.append('XL')
            num -= 40
        elif num >= 10:
            num, res = roman_after(num, 10)
            result += res
        elif num >= 9:
            result.append('IX')
            num -= 9
        elif num >= 5:
            result.append('V')
            num -= 5
            if num > 0:
                result.append(num_to_symbol[num])
            num = 0
        else:
            result.append(num_to_symbol[num])
            num = 0

    return ''.join(result)


def romanToInt(s):
    lst_s = list(s)
    result = 0
    i = 0
    len_s = len(lst_s)
    while i < len_s:
        if lst_s[i] == 'M':
            result += 1000
        elif lst_s[i] == 'D':
            result += 500
        elif lst_s[i] == 'C':
            if i + 1 < len_s:
                if lst_s[i+1] == 'D':
                    result += 400
                    i += 1
                elif lst_s[i+1] == 'M':
                    result += 900
                    i += 1
                else:
                    result += 100
            else:
                result += 100
        elif lst_s[i] == 'L':
            result += 50
        elif lst_s[i] == 'X':
            if i + 1 < len_s:
                if lst_s[i+1] == 'C':
                    result += 90
                    i += 1
                elif lst_s[i+1] == 'L':
                    result += 40
                    i += 1
                else:
                    result += 10
            else:
                result += 10
        elif lst_s[i] == 'V':
            result += 5
        elif lst_s[i] == 'I':
            if i + 1 < len_s:
                if lst_s[i+1] == 'X':
                    result += 9
                    i += 1
                elif lst_s[i+1] == 'V':
                    result += 4
                    i += 1
                else:
                    result += 1
            else:
                result += 1
        i += 1

    return result


def test_roman_to_int():
    result = romanToInt('III')
    print(result)
    result = romanToInt('IV')
    print(result)
    result = romanToInt('IX')
    print(result)
    result = romanToInt('LVIII')
    print(result)
    result = romanToInt('MCMXCIV')
    print(result)
    result = romanToInt('MMMCMXCIV')
    print(result)


test_roman_to_int()


def test_roman():
    result = intToRoman(3)
    print(result)
    result = intToRoman(4)
    print(result)
    result = intToRoman(9)
    print(result)
    result = intToRoman(5)
    print(result)
    result = intToRoman(10)
    print(result)
    result = intToRoman(11)
    print(result)
    result = intToRoman(58)
    print(result)
    result = intToRoman(17)
    print(result)
    result = intToRoman(1994)
    print(result)
    result = intToRoman(3994)
    print(result)

#test_roman()


