class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = sum(gas)
        total_cost = sum(cost)
        start_station = 0
        current_gas = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        return start_station if total_gas >= total_cost else -1


# this version has slightly better runtime, memory is about the same.
