import math
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for data in queries:
            r_point, c_point = data[0], data[1]
            ref_data = data[2]
            tmp = 0
            for ele in points:
                a, b = ele
                compare_data = math.sqrt((a - r_point) * (a - r_point) + (b - c_point) * (b - c_point))
                if compare_data <= ref_data:
                    tmp += 1
            ans.append(tmp)
        return ans

if __name__ == "__main__":
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    print(Solution().countPoints(points, queries))
