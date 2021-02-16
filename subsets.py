from typing import List
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        def get_subsets(location, tmp):
            re.append(tmp)
            for i in range(location, len(nums)):
                get_subsets( i+1, tmp + [nums[i]])
                itertools.permutations



        re = []
        get_subsets(0, [])
        return re


if __name__=="__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))


