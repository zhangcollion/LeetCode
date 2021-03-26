class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = []
        re = float("-inf")
        for idx, value in enumerate(nums):
            if not ans:
                ans.append(value)
            else:
                if ans[-1] < value:
                    ans.append(value)
                else:
                    re =  max(sum(ans), re)
                    ans = []
                    ans.append(value)
        re =  max(sum(ans), re)
        return re