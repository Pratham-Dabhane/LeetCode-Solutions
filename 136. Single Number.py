def singleNumber(nums):
    result = 0
    for num in nums:
        # using bitwise XOR operation
        result ^= num
    return result  