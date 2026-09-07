class Solution(object):
    def climbStairs(self, n):

        dp = [-1] * (n + 1)

        def climb(n, dp):

            if n == 0 or n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]

            first = climb(n-1, dp)
            second = climb(n-2, dp)
            dp[n] = first + second
            return first + second

        return climb(n, dp)