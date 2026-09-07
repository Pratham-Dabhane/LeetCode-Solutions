class Solution(object):
    def rob(self, nums):

        n = len(nums)-1
        dp = [-1] * len(nums)

        def recursive(i):
            if i > n :
                return 0

            else:
                if dp[i] != -1:
                    return dp[i]
                else:                        
                    left = nums[i] + recursive(i+2)
                    right = recursive(i+1)
                    dp[i] = max(left, right) 

                    return dp[i]

        return recursive(0)