from collections import OrderedDict


class Solution:
    def int_to_roman(self, num: int) -> str:

        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def _roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break

        return "".join([a for a in _roman_num(num)])


""" divmod() 
1. Parameters
number1 - numerator, can be an integer or a floating point number
number2 - denominator, can be an integer or a floating point number

2. The method returns:
(quotient, remainder)
"""

if __name__ == "__main__":
    x = Solution()
    print(x.int_to_roman(3))