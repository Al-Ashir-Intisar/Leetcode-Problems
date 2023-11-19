class Solution(object):
    def romanToInt(self, s):
        hash_roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        length = len(s)
        number = 0
        i = 1
        if length == 1:
            return hash_roman_values[s[0]]
        while i < length:
            first_val = hash_roman_values[s[i-1]]
            second_val = hash_roman_values[s[i]]
            if first_val < second_val:
                number += second_val - first_val
                print(first_val, second_val)
                print(number)
                if i+2 < length or i+2 > length:
                    i += 2
                    print(i)
                elif i + 2 == length:
                    last_val = hash_roman_values[s[i+1]]
                    number += last_val
                    print(number)
                    i += 3
                    print(i)
            else:
                if i == length-1:
                    number += first_val +second_val
                    print(first_val, second_val)
                    print(number)
                    i += 1
                    print(i)
                else:
                    number += first_val
                    print(first_val, second_val)
                    print(number)
                    i += 1
                    print(i)
            #print(first_val, second_val)
        print(number)
        return number




solution = Solution()
solution.romanToInt("MCMXCIV")