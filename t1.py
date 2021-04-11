from typing import List
import collections


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            ans *= i
        if ans>0:
             return 1
        elif ans < 0:
            return -1
        else:
            return 0


if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    nums = [[1,2,3],[2],[3],[]]
    print(Solution().arraySign(nums))
