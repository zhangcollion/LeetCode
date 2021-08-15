class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        

        def get_ans(idx, tmp):
            ans.append(tmp)
            for i in range(idx, len(nums)):
                get_ans(i+1, tmp+[nums[i]])
        ans = []
        get_ans(0, [])
       
        return ans