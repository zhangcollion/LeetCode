from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
       
        self.ans = dict()
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        if self.row == 1 or self.col == 1:
            return 0
        self.total = 0
        for i in [0, self.col-1]:
            for j in range(0, self.row):
                if self.grid[i][j] == 1:
                    self.total += 1
                    label = str(i) + "-" + str(j)
                    self.ans[label] = 1
            
        for i in range(1, self.row-1):
            for j in range(1, self.col-1):
                if self.grid[i][j] == 1:
                    self.total += 1
                    label = str(i) + "-" + str(j)
                    if label in self.ans:
                        continue
                    self.cross_point = []
                    self.cross_point.append([(i, j)])
                    self.get_ans((i, j))
        return len(self.ans)

    def get_ans(self, point):
        row, col = point
        for i, j in [(row-1, col),(row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= i < self.row and 0 <= j < self.col and self.grid[i][j] == 1:
                label = str(i) + "-" + str(j)
                if label in self.ans:
                    for c_r, c_l in self.cross_point:
                        self.grid[c_r][c_l] = 0
                        point_label = str(c_r) + "-" + str(c_l)
                        self.ans[point_label] = 1
                        self.cross_point.append([(i, j)])
                        return 
                self.get_ans((i, j))








if __name__=="__main__":
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    obj_solution = Solution()
    ans = obj_solution.numEnclaves(grid)
    print(ans)