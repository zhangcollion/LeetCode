from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        max_ans = 0


        self.result = []
        self.res = []
        self.dfs(heights, rows-1, cols-1, 0, 0)
        return self.result

    def dfs(self, heights, rend, cend, row, col):
         
        if row == rend and col == cend:
            self.result.append(self.res)
            return
        if row-1>=0:
            self.dfs(heights, rend, cend, row-1, col)
            self.res = self.res[0:len(self.res) - 1]
        if row+1<=rend-1:
            self.dfs(heights, rend, cend, row+1, col)
            self.res = self.res[0:len(self.res) - 1]
        if col-1>=0:
            self.dfs(heights, rend, cend, row, col-1)
            self.res = self.res[0:len(self.res) - 1]
        if col+1<=cend-1:
            self.dfs(heights, rend, cend, row, col +1)
            self.res = self.res[0:len(self.res) - 1]


if __name__=="__main__":
    # candidates = [2, 3, 6, 7]
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(Solution().minimumEffortPath(heights))
