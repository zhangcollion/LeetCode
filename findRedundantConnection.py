from typing import List
from collections import defaultdict, Counter
# class Union:
#     def __init__(self, n):
#         self.parent = list(range(n))
#
#     def union(self, idx1, idx2):
#         self.parent[self.find(idx1)] = self.find(idx2)
#
#     def find(self, idx):
#         if self.parent[idx] != idx:
#             self.parent[idx] = self.find(self.parent[idx])
#         return self.parent[idx]
#
#
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         nodesCount = len(edges)
#         parent = list(range(nodesCount + 1))
#
#         def find(index: int) -> int:
#             if parent[index] != index:
#                 parent[index] = find(parent[index])
#             return parent[index]
#
#         def union(index1: int, index2: int):
#             parent[find(index1)] = find(index2)
#
#         for node1, node2 in edges:
#             if find(node1) != find(node2):
#                 union(node1, node2)
#             else:
#                 return [node1, node2]
#
#         return []
#
#
#
class Union:
    def __init__(self,n):
        self.parents = list(range(n))  # 记录每个元素的parent即根节点 先将它们的父节点设为自己
        self.ranks = [0]*n  # 记录节点的rank值

        # 如下图 递归版本 路径压缩(Path Compression)
        # 如果当前的x不是其父节点，就找到当前x的父节点的根节点(find(parents[x])) 并将这个值赋值给x的父节点

    def find(self, x):
        if (x != self.parents[x]):  # 注意这里的if
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # 如下图 根据Rank来合并(Union by Rank)
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # 取rank值小的那个挂到大的那个节点下面，此时两个根节点的rank值并没有发生变化，还是原来的值
        if (self.ranks[rootX] > self.ranks[rootY]):
            self.parents[rootY] = rootX
        if (self.ranks[rootX] < self.ranks[rootY]):
            self.parents[rootX] = rootY
        # 当两个rank值相等时，随便选择一个根节点挂到另外一个跟节点上，但是被挂的那个根节点的rank值需要+1
        if (self.ranks[rootX] == self.ranks[rootY]):
            self.parents[rootY] = rootX
            self.ranks[rootX] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #  使用并查集，将有几个环就是几个有几条线缆
        # 将不再并中的设备加一根线缆，并判断其父节点是不是相同
        if not edges:
            return []
        ans = []
        n = len(edges)
        uf = Union(n)
        for i, j in edges:
            i = i - 1
            j = j - 1
            if uf.find(i) == uf.find(j):
                ans.append([i+1, j+1])
            else:
                uf.union(i ,j )
        print(uf.parents)
        if not ans:
            return ans
        return ans[-1]




if __name__ == "__main__":


    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(Solution().findRedundantConnection(edges))
