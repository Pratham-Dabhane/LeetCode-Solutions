class Solution:

    def solve(self, i, nums, target, prod):
        n = len(nums)
        if i >= n or prod > target:
            return False
        if prod == target:
            return True
        return self.solve(i+1, nums, target, prod*nums[i]) or self.solve(i+1, nums, target, prod)

    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total = 1
        for i in nums:
            total = total * i
        if total != target * target:
            return False
        return self.solve(0, nums, target, 1)