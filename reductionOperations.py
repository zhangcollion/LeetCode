class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ref_data = min(nums)
        data_info  = Counter(nums)
        if len(data_info) == 1:
            return 0
        idx = list(data_info.keys())[1:]
        ans = []
        for i in idx[::-1]:
            if not ans:
                ans.append(data_info[i])
            else:
                ans.append(ans[-1]+data_info[i])
            
        return sum(ans)