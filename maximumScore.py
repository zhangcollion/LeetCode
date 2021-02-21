from typing import List
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        ans = 0
        for i, value in enumerate(multipliers):
            idx = 0
            if value * nums[i] >= i * nums[-1]:
                ans += i * nums[0]
                nums = nums[1:]
            if i * nums[0] < i * nums[-1]:
                ans += i * nums[-1]
                nums = nums[0:-1]
        return ans