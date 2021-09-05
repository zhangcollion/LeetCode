class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nums = board
        self.ans = False
        self.word = word
        self.seen = [[0 for i in range(0, len(board[0]))] for j in range(0, len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):     
                if board[i][j] == word[0] and self.seen[i][j] == 0:
                    self.seen[i][j] = 1
                    self.get_ans(i,j, word[0], 1)
                    self.seen[i][j] = 0
                if self.ans:
                    return self.ans
        return self.ans

    def get_ans(self, rows, cols ,tmp, idx):
        if tmp == self.word:
            self.ans = True
            return
        for i, j in [(rows, cols+1),(rows+1, cols),(rows-1, cols),(rows, cols-1)]:
            if 0<=i< len(self.nums) and 0<=j < len(self.nums[0]) and self.seen[i][j]==0 and self.nums[i][j]==self.word[idx]:
                self.seen[i][j] = 1
                self.get_ans(i, j, tmp+self.word[idx],idx+1)
                self.seen[i][j] = 0
                if self.ans :
                    break