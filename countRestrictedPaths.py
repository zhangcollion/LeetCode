import collections
from typing import List
import heapq


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        if n <= 1:
            return 0
        info = collections.defaultdict(list)
        for u, v, d in edges:
            info[u].append((v, d))
            info[v].append((u, d))
        dp = []
        distance = [float("inf")] * (n + 1)
        distance[n] = 0
        heapq.heappush(dp, [n, 0])
        while dp:
            idx, d = heapq.heappop(dp)
            for i, cost in info[idx]:
                if distance[i] > d + cost:
                    distance[i] = d + cost
                    heapq.heappush(dp, [i, distance[i]])

        new_info = collections.defaultdict(list)
        for u, v, d in edges:
            if distance[v] < distance[u]:
                new_info[u].append((v, d))
            if distance[v] > distance[u]:
                new_info[v].append((u, d))
        self.distance = distance
        self.end = n
        self.info = new_info
        self.d_info = collections.defaultdict(list)
        ans = self.dfs(1)

        return ans % (pow(10, 9) + 7)


    def dfs(self, start):
        if start == self.end:
            return 1
        d = 0
        if start not in self.d_info:
            for i in self.info[start]:
                next_data, _ = i
                if next_data not in self.d_info:
                    if self.distance[start] > self.distance[next_data]:
                        d  +=  self.dfs(next_data)
                    else:
                        d += 0
                else:
                    d += self.dfs(next_data)
            self.d_info[start] = d
            return self.d_info[start]
        else:
            return self.d_info[start]







if __name__=="__main__":
    n = 7
    edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
    print(Solution().countRestrictedPaths(n, edges))


