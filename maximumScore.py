from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        ans = 0
        rows = len(multipliers)
        cols = len(nums)
        boards = [[0 for i in range(cols)] for j in range(rows)]
        for i, value in enumerate(multipliers):
            for j, ref in enumerate(nums):
                boards[i][j] = value * ref
        # print(boards)
        self.goal = rows
        self.ans = []
        self.get_ans(boards, 0, 0, 1, cols - 1, [boards[0][0]])
        self.get_ans(boards, 0, cols - 1, 0 , cols - 1 - 1, [boards[0][cols-1]])
        # print(self.ans)
        for i in self.ans:
            ans = max(ans, sum(i))
        return ans

    def get_ans(self, boards, r, c, ref_s, ref_e, seen):
        if len(seen) == self.goal:
            self.ans.append(seen)
            return
        if 0 <= r + 1 < len(boards) and 0 <= ref_s < len(boards[0]) :
            self.get_ans(boards, r + 1, ref_s, ref_s+1, ref_e , seen + [boards[r + 1][ref_s]])
        if 0 <= r + 1  < len(boards) and 0 <= ref_e < len(boards[0]) :
            self.get_ans(boards, r+1, ref_e, ref_s, ref_e-1 , seen + [boards[r+1][ref_e]])


if __name__ == "__main__":
    nums = [555, 526, 732, 182, 43, -537, -434, -233, -947, 968, -250, -10, 470, -867, -809, -987, 120, 607, -700, 25, -349,
     -657, 349, -75, -936, -473, 615, 691, -261, -517, -867, 527, 782, 939, -465, 12, 988, -78, -990, 504, -358, 491,
     805, 756, -218, 513, -928, 579, 678, 10]
    multipliers = [783, 911, 820, 37, 466, -251, 286, -74, -899, 586, 792, -643, -969, -267, 121, -656, 381, 871, 762, -355, 721, 753,
     -521]
    print(Solution().maximumScore(nums, multipliers))
