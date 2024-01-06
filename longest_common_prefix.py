class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first_len = len(strs[0])
            second_len = len(strs[1])
            min_val = min(first_len, second_len)

            for i in range(min_val):
                a = strs[0][i]
                b = strs[1][i]
                if a == b:
                    prefix += a
                else:
                    break
            if prefix == "":
                return ""
            else:
                for i in range(2, len(strs)):
                    j = 0
                    k = 0
                    while j == 0 and k < len(strs[i]) and k < len(prefix):
                        if strs[i][k] != prefix[k]:
                            j = 1
                        else:
                            k += 1
                    prefix = prefix[:k]


                return prefix




solution = Solution()
result = solution.longestCommonPrefix(["aaa","aa","aaa"])
print(result)
