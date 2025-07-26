class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        prefix_map = {0:1}

        for i in range(len(nums)):

            sum += nums[i]
            rem = sum - k

            if rem in prefix_map:

                res += prefix_map[rem]

            if sum not in prefix_map:
                prefix_map[sum] = 1
            else:
                prefix_map[sum] += 1
        
        return res   