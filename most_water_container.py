class Solution:
    def maxArea(self, height):
        size = len(height)
        water_list = 0
        #print(size)
        left = 0
        right = size - 1
        while right > left:
            lower = min(height[left], height[right])
            area = lower * (right - left)
            if area > water_list:
                water_list = area
            #print(lower)
            #print(area)
            if lower == height[left]:
                left += 1
            elif lower == height[right]:
                right -= 1
        print(water_list)
        return water_list

            



solution = Solution()

result = solution.maxArea([1,1])