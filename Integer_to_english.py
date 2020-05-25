class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        def num_under_thousand(under_thousand, dic):
            under_result = []
            res = under_thousand // 100
            under_thousand %= 100
            if res > 0:
                under_result.append(dic[res])
                under_result.append('Hundred')

            small_divisor = [90, 80,70,60,50,40,30,20,10]
            for sd in small_divisor:
                q = under_thousand // sd
                if q > 0:
                    under_result.append(dic[sd])
                under_thousand %= sd

            if under_thousand > 0:
                under_result.append(dic[under_thousand])

            return under_result

        if num == 0:
            return 'zero'

        num_in_english = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                          9: 'Nine', 10: 'Ten',
                          11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                          16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                          19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                          50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninghty',
                          1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}
        divider = [1000000000, 1000000, 1000]
        result = []
        for div in divider:
            quotient = num // div
            num %= div
            if quotient > 0:
                val = num_under_thousand(quotient, num_in_english)
                result += val
                result.append(num_in_english[div])

        val = num_under_thousand(num, num_in_english)
        result += val

        return ' '.join(result)


def test_():
    t = Solution()
    result = t.numberToWords(12345)
    print(result)

test_()