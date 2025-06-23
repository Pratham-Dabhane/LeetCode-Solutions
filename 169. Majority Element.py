def majorityElement(self, nums: list[int]) -> int: # using hashmap

    frequency_map = {}

    for i in range(len(nums)):

        if nums[i] not in  frequency_map:
            frequency_map[nums[i]] = 1

        else:
            frequency_map[nums[i]] += 1
        
        print(frequency_map)

    return max(frequency_map, key=frequency_map.get)

# ==============Boyer=Moore=Voting=Algorithm===============

def majorityElement(self, nums: list[int]) -> int:

    count = 0
    candidate = None
    
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
            count += 1
        
        elif nums[i] == candidate:
            count += 1
        
        else:
            count -= 1

    return candidate