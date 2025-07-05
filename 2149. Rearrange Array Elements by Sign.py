class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        j = 0
        x = 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])


        while j < len(nums):

            nums[j] = positive[x]
            j += 1
            
            nums[j] = negative[x]
            j += 1

            x += 1

        return nums