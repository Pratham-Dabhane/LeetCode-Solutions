class Solution(object):
    def canJump(self, nums):
        
        max_ind = 0

        for i in range(len(nums)):
            if i > max_ind:
                return False
            else:
                max_ind = max(i + nums[i], max_ind)
        return True        