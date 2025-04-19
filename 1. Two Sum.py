class Solution(object):
    
    def twoSum(self, nums, target):

        numMap = {}

        for i in range(len(nums)):

            diff = target - nums[i] # finds the difference between the target and the current  

            if diff in numMap: # checks if the difference between the numbers already exists in the map

                return [i, numMap[diff]]
            
            numMap[nums[i]] = i # maps the current value and the index in the map