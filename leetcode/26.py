#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        current = nums[0]
        index = 1
        for i in range (1, len(nums)):
            if nums[index] == current:
                nums.pop(index)
            else:
                current = nums [index]
                index += 1
        
        return len(nums)