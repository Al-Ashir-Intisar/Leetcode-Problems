class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_arr = []
        size_m = len(nums1)
        size_n = len(nums2)
        median = None
        merged_lenght = size_m + size_n
        if size_m == 0 and size_n > 0:
            merged_arr = nums2
        elif size_n == 0 and size_m > 0:
            merged_arr = nums1
        else:
            i = 0
            j = 0
            while i < size_m or j < size_n:
                next_m = nums1[i]
                next_n = nums2[j]
                if next_m < next_n:
                    merged_arr.append(next_m)
                    print(next_m)
                    i += 1
                    print(i)
                    if i == size_m:
                        while j < size_n:
                            merged_arr.append(nums2[j])
                            print(nums2[j])
                            j += 1
                            print(j)
                else:
                    merged_arr.append(next_n)
                    print(next_n)
                    j += 1
                    print(j)
                    if j == size_n:
                        while i < size_m:
                            merged_arr.append(nums1[i])
                            print(nums1[i])
                            i += 1
                            print(i)
            print(merged_arr)

        if merged_lenght%2 == 1:
            median = merged_arr[merged_lenght//2]
            print(median)
        else:
            median = (merged_arr[(merged_lenght//2)-1] + merged_arr[merged_lenght//2])/2.0
            print(median)
        return median        




solution = Solution()
nums1 = []
nums2 = [3]
solution.findMedianSortedArrays(nums1, nums2)