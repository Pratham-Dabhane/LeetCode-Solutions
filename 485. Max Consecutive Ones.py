class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        max_count = 0
        count = 0

        for i in nums:

            if i == 1:
                count += 1

            else:
                max_count = max(max_count, count)
                count = 0

        max_count = max(max_count, count)

        return max_count      