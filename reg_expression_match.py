class Solution_1:
    def isMatch(self, s: str, p: str) -> bool:
        check_list = [f"{chr(97 + i)}*" for i in range(26)]
        check_list.append(".*")
        list_p = []
        #print(check_list)
        size_s = len(s)
        size_p = len(p)
        i = 0
        while i < size_p:
            #print(p[i])
            if i+1 < size_p and p[i:i+2] in check_list:
                #print(p[i:i+2])
                list_p.append(p[i:i+2])
                i += 2
            else:
                list_p.append(p[i])
                i += 1            
        return list_p


class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        

solve = Solution()
solution = solve.isMatch("aacdck", "a*.*b*cd*")
print(solution)



solve = Solution()
solution = solve.isMatch("aab", ".*")


print(solution)