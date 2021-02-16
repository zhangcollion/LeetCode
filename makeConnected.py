from typing import List
from collections import defaultdict, Counter
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #  使用并查集，将有几个环就是几个有几条线缆
        # 将不再并中的设备加一根线缆，并判断其父节点是不是相同
        if not connections and n != 0:
            return -1

        uf = Union(n)

        connections.sort()
        for i, j in connections:
            if  uf.find(i) > uf.find(j):
                uf.union(i, j)
            else:
                uf.union(j, i)
        line_num = len(connections)
        # for i in range(n):
        #     uf.parent[i] = uf.find(i)
        print(uf.parents)
        dict_info = Counter(uf.parents)
        use  = 0
        print(uf.parents)
        for i in dict_info.keys():
            use += dict_info.get(i)-1
        need = len(set(uf.parents)) - 1
        left = len(connections) - use
        if left >= need:
            return need
        return -1

if __name__ == "__main__":

    # board = [["a", "a"]]
    # word = "aaa"
    n = 8
    connections = [[0, 6], [2, 3], [2, 6], [2, 7], [1, 7], [2, 4], [3, 5], [0, 2]]
    print(Solution().makeConnected(n, connections))
