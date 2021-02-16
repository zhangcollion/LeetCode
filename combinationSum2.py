from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
        i = start
        while i < len(candidates):
            self.res.append(candidates[i])
            self.get_res(i+1, candidates, target)
            self.res = self.res[0:len(self.res) - 1]
            j = i + 1
            index = i
            while j < len(candidates):
                if candidates[j] == candidates[i]:
                    index = j
                j += 1
            i = index
            i += 1





if __name__=="__main__":
    candidates =  [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))