from typing import List
from collections import  defaultdict
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        info = defaultdict(list)
        for idx, ele in enumerate(tasks):
            start, keep = ele
            info[start].append((keep, idx))
        keys = sorted(info.keys())
        ans = []
        end_time = 0
        pq = []
        for start_time in keys:
            while len(pq) != 0 and end_time < start_time:
                keep, idx, ref_time = heapq.heappop(pq)
                end_time = max(ref_time, end_time) + keep
                ans.append(idx)
            for keep, idx in info[start_time]:
                heapq.heappush(pq, (keep, idx, start_time))
        while len(pq) != 0:
            keep, idx, start_time = heapq.heappop(pq)
            ans.append(idx)
        return ans
if __name__=="__main__":
    tasks =  [[7,10],[7,12],[7,5],[7,4],[7,2]]
    print(Solution().getOrder(tasks))