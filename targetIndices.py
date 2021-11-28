class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i, t in enumerate(nums):
            if t == target:
                ans.append(i)
        return ans