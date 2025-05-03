def rotateArray(nums, k):

    k = k % len(nums)

    def rev(nums,start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    rev(nums, 0, len(nums)-1)
    rev(nums, 0, k-1)
    rev(nums, k, len(nums)-1)