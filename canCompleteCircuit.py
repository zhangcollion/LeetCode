from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            left_gas = 0
            flag = 1
            for i in  range(start, start+len(gas)+1):
                i = i % len(gas)
                left_gas += gas[i]
                left_gas -= cost[i]
                if left_gas < 0:
                    start += 1
                    flag = 0
                    break
            if flag:
                return start
        return -1

if __name__=="__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))