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


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        if n == 0:
            return []
        if n == 1:
            return adjacentPairs[0]

        import collections
        info_adj = collections.defaultdict()
        A2B = collections.defaultdict(list)
        B2A = collections.defaultdict(list)

        for i, j in adjacentPairs:
            if i not in info_adj.keys() or not info_adj:
                info_adj[i] = 0
            if j not in info_adj.keys():
                info_adj[j] = 0
            info_adj[i] = info_adj[i] + 1
            info_adj[j] = info_adj[j] + 1
            A2B[i].append(j)
            B2A[j].append(i)
        for i in info_adj.keys():
            if info_adj[i] == 1:
                ref = i
        ans = [ref]
        while len(ans) <= n:
            if ref in A2B.keys():
                for i in A2B[ref]:
                    if i not in ans:
                        ans.append(i)
            if ref in B2A.keys():
                for i in B2A[ref]:
                    if i not in ans:
                        ans.append(i)
            ref = ans[-1]

        return ans








if __name__ == "__main__":
    adjacentPairs = [[-3,-9],[-5,3],[2,-9],[6,-3],[6,1],[5,3],[8,5],[-5,1],[7,2]]
    print(Solution().restoreArray(adjacentPairs))
