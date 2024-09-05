#88 Merge sorted array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        i2 = n-1
        last = m + n -1
        if len(nums2) != 0:
            for i in range(m+n):
                if nums1[i1] >= nums2[i2] and i1 >= 0 or i2 < 0:
                    nums1[last] = nums1[i1]
                    i1 -= 1
                elif nums1[i1] < nums2[i2] and i2 >= 0 or i1 < 0:
                    nums1[last] = nums2[i2]
                    i2 -= 1
                last -= 1

a = [1,2,3,0,0,0]
Solution().merge(a, 3, [2,5,6], 3)

print(a)