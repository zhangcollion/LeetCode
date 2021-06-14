from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j]=='X') and (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                    count+=1
        return count




if __name__=="__main__":
    candidates =  [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))