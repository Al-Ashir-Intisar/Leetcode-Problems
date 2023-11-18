class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return false if negative numbers 
        if x < 0:
            return False

        #convert the integer to a string 
        str_x = str(x);

        return str_x == str_x[::-1]
    
    #function for checking without converting to string
    def isPalindromeNum(self, x):

        if x< 0:
            return False
        else:
            i = 10
            while i < x: 
                remainder10 = x % i
                if remainder10 != 0:
                    print(remainder10 / (i/10))
                    x = x - remainder10
                    #print(i)
                else:
                    #print(x / i)
                    i = i * 10



    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
solution.isPalindromeNum(12121)