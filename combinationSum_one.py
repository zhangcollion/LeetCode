class Solution:
    def combinationSum(self, nums: List[int], k: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        if nums[0] > k:
            return []
        def get_ans(start, tmp):
            if sum(tmp) == k:
                ans.append(tmp)
                return 
            if sum(tmp) > k:
                return
            for i in range(start,len(nums)):
                get_ans(i, tmp+[nums[i]])
        ans = []
        get_ans(0, [])
        return ans