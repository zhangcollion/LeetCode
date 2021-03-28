class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return board

        nrows = len(board)
        ncols = len(board[0])
        ref = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        res = set()
        for i in range(nrows):
            for j in range(ncols):
                ans = 0
                for ele in ref:
                    a, b = ele
                    m = i + a
                    n = j + b
                    if 0 <= m < nrows and 0 <= n < ncols and board[m][n] == 1:
                        ans += 1
                if board[i][j] == 1:
                    if ans < 2 or ans > 3:
                        res.add((i,j))
                else:
                    if ans == 3:
                        res.add((i,j))
        for i in range(nrows):
            for j in range(ncols):
                if (i, j) in res:
                    if 0 == board[i][j]:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0



