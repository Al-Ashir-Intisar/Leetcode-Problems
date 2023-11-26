#Longest Palindromic Substring
# Given a string s, return the longest 
# palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
class Solution(object):
    def longestPalindrome1(self, s):
        palindrome_size = 0
        palindrome = ""
        temp = ""
        string_size = len(s)
        if string_size == 0:
            return None
        elif string_size == 1:
            return s
        else:
            right = 0
            left = 0
            for i in range(string_size):
                print(s[i])
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""




solution = Solution()
str1 = ""
str2 = "a"
str3 = "ab"
print(solution.longestPalindrome(str1))
print(solution.longestPalindrome(str2))
print(solution.longestPalindrome(str3))