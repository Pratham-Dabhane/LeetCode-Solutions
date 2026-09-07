class Solution(object):
    def twoCitySchedCost(self, costs):

        ans = 0
        fin_cost = []

        for a in range(len(costs)):
            fin_cost.append(costs[a][1] - costs[a][0])
            ans +=  costs[a][0]

        fin_cost.sort()        
        ans += sum(fin_cost[:len(costs)//2])

        return ans