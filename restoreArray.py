from typing import List


# class UnioSet:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#
#     def union(self, idx1, idx2):
#         root1 = self.find(idx1)
#         root2 = self.find(idx2)
#         if self.rank[root1] < self.rank[root2]:
#             self.parent[root2] = root1
#             self.rank[root1] -= 1
#         if self.rank[root1] > self.rank[root2]:
#             self.parent[root1] = root2
#             self.rank[root2] -= 1
#         if self.rank[root1] == self.rank[root2]:
#             self.parent[root2] = root1
#             self.rank[root1] -= 1
#
#     def find(self, idx):
#         if self.parent[idx] != idx:
#             self.parent[idx] = self.find(self.parent[idx])
#         return self.parent[idx]

import collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        if n == 0:
            return []
        if n == 1:
            return adjacentPairs[0]
        dic = collections.defaultdict(list)
        n = len(adjacentPairs) + 1
        for x, y in adjacentPairs:
            dic[x].append(y)
            dic[y].append(x)
        head = [k for k, v in dic.items() if len(v) == 1]
        res = [head[0]]
        while len(res) < n:
            i = res[-1]
            j = dic[i].pop()
            dic[j].remove(i)
            res.append(j)
        return res







if __name__ == "__main__":
    adjacentPairs = [[-3,-9],[-5,3],[2,-9],[6,-3],[6,1],[5,3],[8,5],[-5,1],[7,2]]
    print(Solution().restoreArray(adjacentPairs))
