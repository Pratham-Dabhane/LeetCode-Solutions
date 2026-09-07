class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[1])
        n = len(intervals)
        last_index = intervals[0][1]
        count = 0

        for i in range(1,len(intervals)):
            if intervals[i][0] >= last_index:
                count += 1
                last_index = intervals[i][1]

        return n - count -1