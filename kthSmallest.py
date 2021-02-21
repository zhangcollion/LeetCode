from typing import  List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans.append(matrix[i][j])

        ans.sort()

        return ans[k - 1]

