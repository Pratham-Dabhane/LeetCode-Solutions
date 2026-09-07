class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalGas = sum(gas)
        totalcost = sum(cost)

        if totalcost > totalGas:
            return -1

        curr_gas, start_index = 0,0

        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start_index = i + 1
                curr_gas = 0

        return start_index