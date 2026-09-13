class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        idx = 0
        curr = 0

        for i in range(len(gas)):
            delt = gas[i]-cost[i]
            total += delt
            curr += delt
            if curr < 0:
                idx = i + 1
                curr = 0
        
        return idx if total>=0 else -1