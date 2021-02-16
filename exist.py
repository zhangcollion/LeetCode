from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and not word:
            return True

        word_len = len(word)
        loc = 0
        ref = word[0]
        valid_loc = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ref:
                    valid_loc.append((i, j))
        if word_len == 1 and valid_loc:
            return True
        loc += 1

        def get_ans(graph, c, r, word, loc,seen):
            if loc == len(word):
                return True
            ref = word[loc]
            ref_loc = [(c - 1, r), (c + 1, r), (c, r - 1), (c, r + 1)]
            for m, n in ref_loc:
                if 0 <= m < rows and 0 <= n < cols and ref == board[m][n] and (m,n ) not in seen:
                    re = get_ans(graph, m, n, word, loc+1, seen+[(m,n )])
                    if re:
                        return True
            return False
        seen = []
        for c, r in valid_loc:

            ans = get_ans(board, c, r, word, loc, seen+[(c, r)] )
            if ans:
                return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # board = [["a", "a"]]
    # word = "aaa"
    print(Solution().exist(board, word))
