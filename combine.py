class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        ans = []

        def get_ans(idx, tmp):
            if len(tmp) == k:
                ans.append(tmp)
                return
            for i in range(idx, len(nums)):
                get_ans(i+1, tmp+[nums[i]])

        get_ans(0, [])
        return ans