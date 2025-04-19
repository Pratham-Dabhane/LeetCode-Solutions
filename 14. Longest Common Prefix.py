class Solution(object):
    def longestCommonPrefix(self, strs):

        result = ""

        for i in range (len(strs[0])): # this for loop only iterates till the length of the first string in strs

            for s in strs: # this loop iterates through all the strings in the strs

                if i == len(s) or s[i] != strs[0][i]: # checks if the ith character of the sting s is not equal to ith character of 0th index string in strs
                    return result
                
            result += strs[0][i]

        return result