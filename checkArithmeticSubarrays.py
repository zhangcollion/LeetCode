from typing import *
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        if not nums or not l or not r:
            return [False]

        res = []
        for i, j in zip(l,r):
            s = slice(i, j+1)
            data = nums[s]
            res.append(self.is_subarray(data))


        return res

    def is_subarray(self, data):
        data.sort()
        if len(data) == 1:
            return True
        ref = data[1]-data[0]
        for i in range(1, len(data)):
            if data[i]-data[i-1] != ref:
                return False
        return True

if __name__ == "__main__":
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(Solution().checkArithmeticSubarrays(nums, l, r))
