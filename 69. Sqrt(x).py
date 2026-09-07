class Solution(object):
    def mySqrt(self, x):
        
        low = 1
        high = x

        while low <= high:
            mid = (low + high) // 2

            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            
            elif mid_sq > x:
                high = mid - 1

            else:
                low = mid + 1
        return high