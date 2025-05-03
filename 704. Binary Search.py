def binarySearch(nums, target):

    start, end = 0, len(nums)-1

    while start <= end:

        mid = (start + end)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            end = mid -1 
        
        else:
            start = mid + 1
        
    return -1


nums = [3, 4, 6, 7, 9, 12, 16, 17, 18]
target = 6

print(binarySearch(nums, target))