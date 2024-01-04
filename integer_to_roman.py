class Solution:
    def intToRoman(self, num):
        roman = ""
        div = num//1000
        if div > 0:
            for i in range(div):
                roman = roman + "M"
                num -= 1000
        div = num//900
        if div > 0:
            for i in range(div):
                roman = roman + "CM"
                num -= 900
        div = num//500
        if div > 0:
            for i in range(div):
                roman = roman + "D"
                num -= 500
        div = num//400
        if div > 0:
            for i in range(div):
                roman = roman + "CD"
                num -= 400
        div = num//100
        if div > 0:
            for i in range(div):
                roman = roman + "C"
                num -= 100
        div = num//90
        if div > 0:
            for i in range(div):
                roman = roman + "XC"
                num -= 90
        div = num//50
        if div > 0:
            for i in range(div):
                roman = roman + "L"
                num -= 50
        div = num//40
        if div > 0:
            for i in range(div):
                roman = roman + "XL"
                num -= 40
        div = num//10
        if div > 0:
            for i in range(div):
                roman = roman + "X"
                num -= 10
        div = num//9
        if div > 0:
            for i in range(div):
                roman = roman + "IX"
                num -= 9
        div = num//5
        if div > 0:
            for i in range(div):
                roman = roman + "V"
                num -= 5
        div = num//4
        if div > 0:
            for i in range(div):
                roman = roman + "IV"
                num -= 4
        div = num//1
        if div > 0:
            for i in range(div):
                roman = roman + "I"
                num -= 1


        return roman
        








solution = Solution()
result = solution.intToRoman(1994)

print(result)