class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = len(nums)//2
        ans = []
        for i in range(left):
            ans.append(nums[i]+nums[len(nums)-i-1])
        return max(ans)