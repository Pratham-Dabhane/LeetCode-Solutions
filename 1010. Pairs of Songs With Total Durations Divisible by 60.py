class Solution(object):
    def numPairsDivisibleBy60(self, time):
        count = 0
        rem2count = [0] * 60

        for x in time:
            rem = x % 60

            if rem == 0:
                count += rem2count[0]

            else:
                count += rem2count[60-rem]

            rem2count[rem] += 1
        return count
        