from typing import List
import collections
import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []
        n = len(intervals)
        if 1 == n:
            return [-1]

        info = collections.defaultdict()
        k = 0
        for i in intervals:
            m, n = i
            info[m] = k
            k += 1

        sorted(info.items(), key=lambda x:info.keys(), reverse=True)
        print(info)
        data = list(info.keys())
        ans =[]
        for i in intervals:
            m, n = i
            idx = bisect.bisect_left(data, n)
            ans.append(idx)

        return ans