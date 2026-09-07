class Solution(object):
    def search(self, nums, target):

        low, high = 0, len(nums)-1

        while high >= low:

            mid = (high + low)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1