from typing import List
from  collections import defaultdict
a = defaultdict()
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        start = 0
        self.res = []
        candidates.sort()
        self.get_res(start, candidates, target)
        return self.result

    def get_res(self, start, candidates, target):
        if sum(self.res) == target:
            self.result.append(self.res)
            return
        if sum(self.res) > target:
            return
        for i in range(start, len(candidates)):
            self.res.append(candidates[i])
            self.get_res(i, candidates, target)
            self.res = self.res[0:len(self.res) - 1]







if __name__=="__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))