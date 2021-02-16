from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        re = []
        def get_permute(tmp, index):
            if len(tmp) == len(nums):
                re.append(tmp)
                return
            for i in range(0, len(nums)):
                if i not in index:
                    get_permute( tmp+[nums[i]], index+[i])
        get_permute([], [])
        return r


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))