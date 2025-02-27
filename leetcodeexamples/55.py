# 55. Jump game

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        jumping = True
        position = 0
        jump_length = nums[0]
        while jump_length >= 0:
            if jump_length == 0 :
                return False
            position += 1
            jump_length -= 1
            if position >= len(nums) - 1:
                return True
            if nums[position] > jump_length:
                jump_length = nums[position]