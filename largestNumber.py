import functools
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1
            if s1 + s2 < s2 + s1:
                return 1
            return 0

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(compare))
        re = "".join(nums)
        i = 0
        while i < len(re) - 1:
            if re[i] == "0":
                i += 1
            else:
                break
        re = re[i:]
        return re