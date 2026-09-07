class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()

        m = len(players)
        n = len(trainers)

        l, r = 0, 0

        while(l < m and r < n ):
            if (players[l] <= trainers[r]):
                l += 1
            r += 1

        return l