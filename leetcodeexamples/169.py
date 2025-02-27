# 169. Majority Element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        global_max = 0
        current_max = 1
        maj = nums[0]
        element = nums[0]
        for i in range (1, len(nums)):
            if nums[i] == element:
                current_max += 1
                if current_max > global_max:
                    global_max = current_max
                    maj = element
            else:
                current_max = 1
                element = nums[i]
        
        return maj