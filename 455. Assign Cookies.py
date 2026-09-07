class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        l, r = 0, 0

        while(l < m and r < n ):
            if (g[l] <= s[r]):
                l += 1
            r += 1

        return l