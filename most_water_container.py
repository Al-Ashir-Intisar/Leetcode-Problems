class Solution:
    def maxArea(self, height):
        size = len(height)
        water_list = []
        #print(size)
        left = 0
        right = size - 1
        while right > left:
            lower = min(height[left], height[right])
            area = lower * (right - left)
            water_list.append(area)
            #print(lower)
            #print(area)
            if lower == height[left]:
                left += 1
            elif lower == height[right]:
                right -= 1
            maximum = max(water_list)
        print(maximum)
        return maximum

            



solution = Solution()

result = solution.maxArea([1,1])