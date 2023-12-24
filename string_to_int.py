class Solution:
    def myAtoi(self, s: str) -> int:
        def helper(index):
            if index == len(s):
                return 0, index

            # Skip leading whitespaces
            while index < len(s) and s[index].isspace():
                index += 1

            # Check for optional sign
            if index < len(s) and (s[index] == '+' or s[index] == '-'):
                sign = -1 if s[index] == '-' else 1
                index += 1
            else:
                sign = 1

            result = 0

            # Process digits
            while index < len(s) and s[index].isdigit():
                result = result * 10 + int(s[index])
                index += 1

            return sign * result, index

        result, _ = helper(0)
        return max(min(result, 2**31 - 1), -2**31)


solution = Solution()

print(solution.myAtoi("    -42"))