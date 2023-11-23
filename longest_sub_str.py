class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string

        # Create a dictionary with all letters, digits, symbols, and spaces, and set their values to 0
        all_characters = string.ascii_letters + string.digits + string.punctuation + ' '
        character_values = {char: 0 for char in all_characters}

        temp = [] 
        max = 0
        size = 0
        lenght = len(s)
        i = 0
        j = 0
        while j < lenght:
            if character_values[s[j]] == 0:
                #print(s[j])
                temp.append(s[j])
                character_values[s[j]] = 1
                size = len(temp)
                #print(size)
                if size > max:
                    max = size
                j += 1
            elif character_values[s[j]] == 1:
                size = len(temp)
                #print(size)
                if size > max:
                    max = size
                character_values = {char: 0 for char in all_characters}
                temp = []
                size = 0
                i += 1
                j = i
        if lenght > 0 and max == 0:
            max = lenght
        #print(max)


        # Print the dictionary
        #print(temp)
        #print(character_values)
        return max
    #better function solution
    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength




solution = Solution()
print(solution.lengthOfLongestSubstring1("abcabcbb"))