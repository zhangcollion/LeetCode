class Solution:
    def combinationSum2(self, nums: List[int], k: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        if nums[0] > k:
            return []
        if sum(nums) < k:
            return []
        def get_ans(idx, tmp):
            if sum(tmp) > k:
                return 
            if sum(tmp) == k :
                ans.append(tmp)
                return
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                get_ans(i+1, tmp+[nums[i]])

        ans = []
        get_ans(0, [])
        return ans