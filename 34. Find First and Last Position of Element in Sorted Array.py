class Solution(object):
    def searchRange(self, nums, target):
        def findFirst():
            low = 0
            high = len(nums) - 1
            first = -1

            while high >= low:
                mid = low + (high - low) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    first = mid
                    high = mid - 1
            return first


        def findLast():
            low = 0
            high = len(nums) - 1
            last = -1

            while high >= low:
                mid = low + (high - low) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    last = mid
                    low = mid + 1
            return last

                
        return [findFirst(), findLast()]