class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n_row = len(rowSum)
        n_col = len(colSum)
        ans = [[0 for i in range(n_col)] for j in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                min_num = min(rowSum[i], colSum[j])
                ans[i][j] = min_num
                rowSum[i] -= min_num
                colSum[j] -= min_num

        return ans