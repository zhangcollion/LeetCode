from typing import  List
import collections
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        info = collections.defaultdict()
        for i in nums:
            if i not in info.keys():
                info[i] = 1
            else:
                info[i] += 1

        for i, v in info.items():
            if v == 1:
                return i

        return -1

