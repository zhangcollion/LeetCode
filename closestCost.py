from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        useful_base = []
        for i in baseCosts:
            if i <= target:
                useful_base.append(i)
        if not useful_base:
            return min(baseCosts)
        if max(useful_base) == target:
            return target

        self.useful_topping = toppingCosts
        self.ans = []
        ans = 0
        self.com = float("inf")
        for i in baseCosts:
            self.useful_cnt = [1] * len(self.useful_topping)
            self.dfs([i], 0)
        re = [sum(ele) for ele in self.ans]
        re.sort()
        for ele in re:
            if abs(ele - target) < self.com:
                self.com = abs(ele - target)
                ans = ele
        return ans

    def dfs(self, res, idx):
        self.ans.append(res)
        for top_idx in range(idx, len(self.useful_topping)):
            if self.useful_cnt[top_idx] < 3:
                self.useful_cnt[top_idx] += 1
                self.dfs(res + [self.useful_topping[top_idx]], top_idx)
                self.useful_cnt[top_idx] -= 1
            else:
                continue
        return

if __name__ == "__main__":
    baseCosts = [4]
    toppingCosts = [9]
    target = 9

    # baseCosts = [2,3]
    #
    #
    # toppingCosts = [4,5,100]
    # target = 18
    s = Solution()
    print(s.closestCost(baseCosts, toppingCosts, target))
