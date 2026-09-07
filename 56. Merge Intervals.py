class Solution(object):
    def merge(self, intervals):

        if not intervals:
            return []
        elif len(intervals) == 1:
            return intervals

        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        i = 0
        res = []

        while i < len(intervals)-1:

            if intervals[i+1][0] > end:

                res.append([start, end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]

            else:
                end = max(end, intervals[i+1][1])

            i += 1
            
        res.append([start, end])

        return res