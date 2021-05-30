import heapq
from typing import List
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        m = len(tasks)
        free = [(servers[i], i) for i in range(0, len(servers))]
        heapq.heapify(free)
        busy = []
        heapq.heapify(busy)

        ans = [-1]*m
        now = 0
        for i, t in enumerate(tasks):
            now = max(now, i)
            while busy and busy[0][0] <= now:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w,idx))
            if free:
                w, idx = heapq.heappop(free)
                heapq.heappush(busy, (now+t, w, idx))
                ans[i] = idx
            else:
                now, w, idx = heapq.heappop(busy)
                heapq.heappush(busy, (now+t, w, idx))
                ans[i] = idx

        return ans
