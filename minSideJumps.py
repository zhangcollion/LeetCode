from typing import List
from collections import defaultdict


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        if 2 not in obstacles:
            return 0
        n = len(obstacles) - 1
        data1 = []
        data2 = []
        data3 = []
        for idx, valid in enumerate(obstacles):
            if valid == 1:
                data1.append(idx)
            if valid == 2:
                data2.append(idx)
            if valid == 3:
                data3.append(idx)

        next_point = min(data1[-1], data2[-1], data3[-1])



if __name__ == "__main__":
    obstacles = [0, 2, 1, 0, 3, 0]
    print(Solution().minSideJumps(obstacles))