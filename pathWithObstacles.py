class Solution:
    def pathWithObstacles(self, nums: List[List[int]]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        if nums[0][0] == 0:
            self.get_ans(0,0, [])
            if self.ans:
                return self.ans
            else:
                return []
        else:
            return []

    def get_ans(self, rows, cols ,tmp):
        if rows+1==len(self.nums) and cols+1==len(self.nums[0]):
            self.ans = tmp
            return
        for i, j in [(rows, cols+1),(rows+1, cols)]:
            if i< len(self.nums) and j < len(self.nums[0]) and self.nums[i][j]==0:
                self.nums[i][j] = 1
                self.get_ans(i, j, tmp+[[i, j]])
                if self.ans :
                    break