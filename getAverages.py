class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n =  len(nums)
        if n+1 < k:
            return [-1]*n
        if k == 0:
            return nums
        
        ans = []
        ref_data = list(range(k, n-k))
        ans = [-1]*n
        tmp_data = [0]
        res = 0
        for i, data in enumerate(nums):
            res += data
            tmp_data.append(res)
        for i in ref_data:
            ans[i] = (tmp_data[i+k+1]-tmp_data[i-k])//(2*k+1)
        return ans