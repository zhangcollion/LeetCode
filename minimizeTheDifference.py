from typing import List
from  collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.ans = 0
        self.info = defaultdict(list)
        self.seen = [0] * (len(self.nums) + 1)
        self.get_ans(0, [])
        return self.ans

    def get_ans(self, idx, tmp):
        if idx + 1 in self.info and idx + 1 != len(self.nums):
            for tmp_info in self.info[idx + 1]:
                if sum(tmp) + tmp_info == self.target:
                    self.ans += 1
            return
        if len(tmp) == len(self.nums):
            self.info[idx].append(self.nums[-1])
            self.info[idx].append(self.nums[-1] * -1)
            self.seen[idx] = 1
        if sum(tmp) == self.target and idx == len(self.nums):
            self.ans += 1
            return
        if idx == len(self.nums):
            return
        for tmp_token in [1, -1]:
            self.get_ans(idx + 1, tmp + [tmp_token * self.nums[idx]])
            if idx > 0 and idx + 1 <= len(self.nums) and self.seen[idx] == 0:
                for tmp_data in self.info[idx + 1]:
                    self.info[idx].append(tmp[-1] + tmp_data)
                    self.info[idx].append(-1 * tmp[-1] + tmp_data)
                self.seen[idx] = 1



if __name__=="__main__":
    candidates = [47,30,12,40,10,31,5,12,14,25,45,34,34,31,20,1,33,28,30,30]

    target = 34
    print([1]*2)
    print(Solution().findTargetSumWays(candidates, target))