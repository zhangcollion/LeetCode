from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board

        rows = len(board)
        cols = len(board[0])
        m, n = click
        if board[m][n] == "M":
            board[m][n] = "X"
            return board
        dp = []
        dp.append(click)
        while dp:
            length = len(dp)
            while length > 0:
                length -= 1
                m, n = dp.pop(0)
                ref = [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1), (m - 1, n - 1), (m - 1, n + 1), (m + 1, n - 1),
                       (m + 1, n + 1)]
                flag = 1
                cnt = 0
                for i, j in ref:
                    if 0 <= i < rows and 0 <= j < cols:
                        if board[i][j] == "M":
                            cnt += 1
                            flag = 0
                if cnt:
                    board[m][n] = cnt
                if flag:
                    board[m][n] = "B"
                    for i, j in ref:
                        if 0 <= i < rows and 0 <= j < cols and board[i][j] == "E":
                            dp.append((i, j))

        return board


if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    heights = [['E', 'E', 'E', 'E', 'E'],
               ['E', 'E', 'M', 'E', 'E'],
               ['E', 'E', 'E', 'E', 'E'],
               ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    print(Solution().updateBoard(heights, click))
