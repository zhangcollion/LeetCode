from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ans = 0

        rows = len(grid)
        cols = len(grid[0])
        start_points = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    start_points.append((i, j))
        self.ans = -100

        for start_point in start_points:
            m, n = start_point
            self.get_ans(m,n,grid,[grid[m][n]], [(m,n)])

        return self.ans

    def get_ans(self, r, c, grid, data, seen):
        flag = 0
        for (i, j) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and 0 != grid[i][j] and (i, j) not in seen:
                self.get_ans(i, j, grid, data + [grid[i][j]], seen+[(i,j)] )
                flag = 1
        if 0 == flag:
            self.ans = max(self.ans, sum(data))
            return


if __name__ == "__main__":
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(Solution().getMaximumGold(grid))