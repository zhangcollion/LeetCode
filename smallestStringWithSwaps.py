from typing import List
import collections


class UnionSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def union(self, idx1, idx2):
        root1 = self.find(idx1)
        root2 = self.find(idx2)
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        if self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        if self.rank[root1] == self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += 1

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s

        n = len(s)
        uf = UnionSet(n)
        for i, j in pairs:
            uf.union(i, j)

        for i in range(n):
            uf.parent[i] = uf.find(i)

        info = collections.defaultdict(list)
        for i in range(n):
            info[uf.parent[i]].append(i)
        str_data = list(s)
        for i in info.keys():
            idx = info[i]
            ref = [str_data[i] for i in idx]
            ref.sort()
            k = 0
            for j in idx:
                str_data[j] = ref[k]
                k += 1

        return "".join(str_data)


if __name__ == "__main__":
    s = "dcab"
    pairs = [[0, 3], [1, 2]]

    print(Solution().smallestStringWithSwaps(s, pairs))
