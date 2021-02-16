from typing import List
from collections import defaultdict

"""
1. get two islands and remember every points of island
2. get each in  one island, calc steps to another
"""


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A:
            return 0

        rows = len(A)
        cols = len(A[0])

        bridge_location = []
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    bridge_location.append((i, j))
        # get island one and two

        island = []
        while bridge_location:
            island_info = [bridge_location.pop()]
            island_data = [island_info[0]]

            while island_info:
                m, n = island_info.pop()
                A[m][n] = -1
                for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                    if 0 <= i < rows and 0 <= j < cols and A[i][j] == 1:
                        island_info.append((i, j))
                        island_data.append((i, j))
                        A[i][j] = -1
                        if (i, j) in bridge_location:
                            bridge_location.remove((i, j))
            island.append(island_data)

        # calc every point's distance in one island to another, get the min
        min_ans = float("inf")
        ref = island[0]
        left = island[1]
        if len(ref) > len(left):
            ref, left = left, ref

        for data in ref:
            dp = [data]
            steps = 0
            flag = 0
            seen = []
            while dp:
                leng = len(dp)
                for _ in range(leng):
                    m, n = dp.pop(0)
                    for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                        if 0 <= i < rows and 0 <= j < cols:
                            if (i, j) in left:
                                min_ans = min(steps, min_ans)
                                if 1 == min_ans:
                                    return 1
                                dp.clear()
                                flag = 1
                                break
                            if A[i][j] == 0:
                                if (i, j) not in seen or not seen:
                                    seen.append((i, j))
                                    dp.append((i, j))
                    if flag == 1:
                        break
                steps += 1

        return min_ans



if __name__=="__main__":
    A = [[0,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]

    print(Solution().shortestBridge(A))

