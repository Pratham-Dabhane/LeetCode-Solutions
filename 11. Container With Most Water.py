class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            width = right - left
            curr_area = width * min(height[left], height[right])
            max_area = max(max_area, curr_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    


""" Method 2 WITHOUT using min() and max() lookups to save time """    


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            width = right - left

            if height[left] < height[right]:
                curr_area = width * height[left]
                left += 1
            
            else:
                curr_area = width * height[right]
                right -= 1
            
            if curr_area > max_area:
                max_area = curr_area
                
        return max_area