class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        rev_num = 0

        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x = x // 10

        rev_num = rev_num * sign

        rev_bin = bin(rev_num)[2:]
        bit_len = len(rev_bin)

        if sign == -1 and bit_len == 32:
            return rev_num
        elif bit_len <= 31:
            return rev_num 
        else:
            return 0




solution = Solution()

print(solution.reverse(-2147483412))
