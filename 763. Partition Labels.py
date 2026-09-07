class Solution(object):
    def partitionLabels(self, s):
        charMap = {}
        partitions = []
        for l in range(len(s)):
            charMap[s[l]] = l

        i,j = 0,0
        while i < len(s):
            startIndex = i
            endIndex = charMap[s[i]]

            while j <= endIndex:
                lastIndexOfNext = charMap[s[j]]

                if lastIndexOfNext > endIndex:
                    endIndex = lastIndexOfNext

                j += 1

            partitions.append(endIndex - startIndex +1)
            i = endIndex + 1

        return partitions