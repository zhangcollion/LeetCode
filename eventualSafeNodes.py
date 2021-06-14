from typing import List
from collections import Counter
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        mark = [0] * n  

        def helper(p):
            if not graph[p] :
                mark[p] = 1
                return True
            mark[p] = -1
            for node in graph[p]:
                if mark[node] == 1:
                    continue
                if  mark[node] == -1  or not helper(node):
                    return False
            mark[p] = 1
            return True
      
        for i in range(n):
            if mark[i] == 0:
                helper(i)
        return [i for i in range(n) if mark[i] == 1]