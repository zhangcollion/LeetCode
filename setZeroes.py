class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    ans.append((i, j))

        def get_ans(r, c, direction):
            m, n = r + direction[0], c + direction[1]
            if 0 <= m < rows and 0 <= n < cols:
                if matrix[m][n] != 0:
                    matrix[m][n] = 0
                get_ans(m, n, direction)
            return

        ref = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for ele in ans:
            m, n = ele
            for direction in ref:
                get_ans(m, n, direction)
