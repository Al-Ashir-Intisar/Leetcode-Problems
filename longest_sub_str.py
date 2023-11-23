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
                print(s[j])
                temp.append(s[j])
                character_values[s[j]] = 1
                size = len(temp)
                print(size)
                if size > max:
                    max = size
                j += 1
            elif character_values[s[j]] == 1:
                size = len(temp)
                print(size)
                if size > max:
                    max = size
                character_values = {char: 0 for char in all_characters}
                temp = []
                size = 0
                j -= 1
        if lenght > 0 and max == 0:
            max = lenght
        print(max)


        # Print the dictionary
        print(temp)
        #print(character_values)
        return max





solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")