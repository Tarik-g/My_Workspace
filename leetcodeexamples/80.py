# 80. Remove Duplicates from Sorted Array II
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
        appearance_counter = 1
        for i in range (1, len(nums)):
            if nums[index] == current:
                appearance_counter += 1
                if appearance_counter >= 3:
                    nums.pop(index)
                else:
                    index += 1
            else:
                current = nums [index]
                appearance_counter = 1
                index += 1
        
        return len(nums)