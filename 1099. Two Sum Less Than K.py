def TwoSum(nums, target):

    nums = sorted(nums)

    l = 0
    r = len(nums)-1
    max_sum = -1

    while l < r:

        num_sum = nums[l] + nums[r]

        if num_sum >= target:
            r -= 1

        elif num_sum < target:
            max_sum = max(max_sum, num_sum)
            l += 1
            
    return(max_sum)