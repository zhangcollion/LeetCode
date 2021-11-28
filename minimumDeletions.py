class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_data = max(nums)
        min_data = min(nums)
        max_loc = nums.index(max_data)
        min_loc = nums.index(min_data)
        lef_loc = min(max_loc, min_loc)
        rig_loc = max(max_loc, min_loc)
        ans1 = rig_loc+1
        n = len(nums)
        ans2 = max(n-rig_loc, n-lef_loc)
        ans3 = lef_loc+1+n-rig_loc
        return min(ans1, ans2, ans3)