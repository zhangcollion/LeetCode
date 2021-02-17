from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        # ans = [1][[1+i ]  for i in cols for j in rows]
        ans = [[1 for i in range(cols)] for j in range(rows)]
        
        return ans


if __name__ == "__main__":
    rowSum = [3, 8]
    colSum = [4, 7]
    print(Solution().restoreMatrix(rowSum, colSum))
