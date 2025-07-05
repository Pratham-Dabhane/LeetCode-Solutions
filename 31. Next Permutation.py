class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pivot_index = -1

        for i in range (n-2,-1, -1):
            if nums[i] < nums[i+1]:
                pivot_index = i
                break
        
        if pivot_index == -1:
            nums.reverse()
            return
        
        for j in range(n-1, pivot_index, -1):
            if nums[j] > nums[pivot_index]:
                nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
                break

        nums[pivot_index+1:] = reversed(nums[pivot_index+1:])