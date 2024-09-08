# 27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        n = len(nums)
        index_of_vals = []
        for i in range (n):
            if nums[i] != val and len(index_of_vals) != 0:
                nums[index_of_vals[0]] = nums[i]
                index_of_vals.pop(0)
                index_of_vals.append(i)
            elif nums[i] == val:
                k += 1
                index_of_vals.append(i)
        k = n - k
        return k
    
a = [0,1,2,2,3,0,4,2]
ka = Solution().removeElement(a, 2)
print(ka)
print(a)