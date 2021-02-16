from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if not connections:
            return 0
        link_info = defaultdict(set)
        node_info = defaultdict(set)
        for i, j in connections:
            link_info[i].add(j)
            node_info[j].add(i)

        dp = [0]
        seen = set(dp)
        ans = 0
        while dp:
            node = dp.pop()
            for i in link_info[node] | node_info[node]:
                if i not in seen:
                    if node not in link_info[i] :
                        ans += 1
                    seen.add(i)
                    dp.append(i)

        return  ans



if __name__ == "__main__":
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    print(Solution().minReorder(n, connections))