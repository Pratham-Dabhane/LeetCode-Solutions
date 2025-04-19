class Solution(object):
    def moveZeroes(self, nums):
        zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1

        for i in range(zero_index, len(nums)):
            nums[i] = 0
                 
sol = Solution()
nums = [0, 1, 0, 3, 12]
# nums = [0, 0, 3, 3, 5, 6]
sol.moveZeroes(nums)

print(nums)