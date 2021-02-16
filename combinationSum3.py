from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        start = 0
        self.res = []
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.get_res(start, k, n)
        return self.result

    def get_res(self, start, k, n):
        if sum(self.res) > n:
            return
        if sum(self.res) != n and len(self.res) == k:
            return
        if sum(self.res) == n and len(self.res) == k:
            self.result.append(self.res)
            return
        for i in range(start, len(self.candidates)):
            self.res.append(self.candidates[i])
            self.get_res(i+1, k, n)
            self.res = self.res[0:len(self.res) - 1]




if __name__=="__main__":
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))