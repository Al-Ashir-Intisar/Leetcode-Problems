import math
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

        if x < 0:
            return False
        elif x >= 0 and x <10:
            return True
        else:
            log_num = math.log10(x)
            int_log_num = int(log_num)
            power = int_log_num

            i = 1
            number = x
            palindrome = 0
            max = power
            while i <= power:
                remainder = number % (10**i)
                print(remainder)
                palindrome += (10**(max))*(remainder//(10**(i-1)))
                print(palindrome)
                max -= 1
                number -= remainder
                #print(i)
                i += 1
            print(number//(10**(i-1)))
            palindrome += number//(10**(i-1))*(10**max)
            print(palindrome)
            return x == palindrome

        
        




    
solution = Solution()
#print(solution.isPalindrome(121))
#print(solution.isPalindrome(-121))
#print(solution.isPalindrome(10))
print(solution.isPalindromeNum(0000000))