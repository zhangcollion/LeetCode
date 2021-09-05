class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.ans = 0
        self.target = target
        self.toppingCosts = toppingCosts
        self.min_data = 10000
        for cost in baseCosts:
            self.get_ans(0, [cost])

        return self.ans

    def get_ans(self, idx, tmp):
        if sum(tmp) >= self.target:
            if abs(sum(tmp) - self.target) < self.min_data:
                self.min_data = abs(sum(tmp) - self.target)
                self.ans = sum(tmp)
            return
        if abs(sum(tmp) - self.target) <= self.min_data and sum(tmp) - self.target <= 0:
            self.min_data = abs(sum(tmp) - self.target)
            self.ans = sum(tmp)
        if idx >= len(self.toppingCosts):
            return
        for tmp_cost in range(3):
            self.get_ans(idx + 1, tmp + [self.toppingCosts[idx]] * (tmp_cost))

