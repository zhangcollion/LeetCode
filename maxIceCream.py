class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if costs[0] > coins:
            return 0
        ans = 0
        for i in costs:
            if coins >= i:
                ans += 1
                coins -= i
            else:
                break

        return ans