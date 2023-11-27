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
        palindrome_right = 0
        palindrome_left = 0
        palindrome_size = 0
        string_size = len(s)
        if string_size == 0:
            return ""
        elif string_size == 1:
            return s
        else:
            for size in range(string_size+1):
                #print(s[i])
                print(size)
                end = size 
                bool_pal = 0
                while end <= string_size:
                    #print(s[end-size:end])
                    left = end - size 
                    right = end - 1
                    if left == right:
                        bool_pal = 1
                    #print(left, right)
                    while left < right:
                        if s[left] != s[right]:
                            bool_pal = 0
                            left = 0
                            right = 0
                        else:
                            bool_pal = 1
                            left += 1
                            right -= 1
                    if bool_pal == 1:
                        #print(s[end-size:end], " yes")
                        if size > palindrome_size:
                            palindrome_size = size
                            palindrome_left = end - size
                            palindrome_right = end
                        #return s[end-size:end]
                    end += 1
            print(s[palindrome_left:palindrome_right])
            return(s[palindrome_left:palindrome_right])
            



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
str2 = "ab"
str3 = "abaaaa"
#print(solution.longestPalindrome(str1))
#print(solution.longestPalindrome(str2))
solution.longestPalindrome1(str3)