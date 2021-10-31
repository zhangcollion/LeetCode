from typing import List
from collections import defaultdict


class Solution:
    def     (self, nums: List[int]) -> int:
        for i, data in enumerate(nums):
            if mod(i, 10) == data:
                return i

        return -1


