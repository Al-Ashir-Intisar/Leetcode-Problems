class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        size_s = len(s)
        size_p = len(p)
        if size_p > 0:
            last = p[-1]
            if size_p > 1:
                last_1 = p[-2]
                print(last_1)
            print(last)
            if last == ".":
                return True
            elif last == "*" and last_1 == ".":
                return True
            elif last == "*" and last_1 != ".":
                for i in range(size_s):
                    if s[i] != last_1:
                        return False
                return True
            elif last not in ("*", "."):
                if size_p != size_s:
                    return False
                else:
                    for i in range(size_s):
                        if s[i] != p[i]:
                            return False
                    return True




solve = Solution()
solution = solve.isMatch("aa", "b*")


print(solution)