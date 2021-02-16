from typing import List
from collections import defaultdict
"use 回溯超时   "

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         "use dijkstra to get cost , but constrain in steps"
#         ans = -1
#         if not flights and src == dst:
#             return ans
#         flights_info = defaultdict(list)
#         for u, v, w in flights:
#             flights_info[u].append((v, w))
#         res = []
#         cost = 0
#         steps = 0
#
#         def get_ans(flights_info, src, dst, K, res, cost, steps):
#             if src == dst and steps <= K+1:
#                 res.append(cost)
#                 return
#             if steps > K+1:
#                 return
#             data = flights_info[src]
#             if not data:
#                 return
#             for start, money in data:
#                 get_ans(flights_info, start, dst, K, res, cost + money, steps + 1)
#
#         get_ans(flights_info, src, dst, K, res, cost, steps)
#         if res:
#             return min(res)
#         return -1
#
#
# if __name__ == "__main__":
#     n = 3
#     edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
#     src = 0
#     dst = 2
#     k = 0
#     print(Solution().findCheapestPrice(n, edges, src, dst, k))



import queue, heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        "use dijkstra to get cost , but constrain in steps"
        # ans = -1
        # if not flights and src == dst:
        #     return ans
        # flights_info = defaultdict(list)
        # for u, v, w in flights:
        #     flights_info[u].append((v, w))
        #
        # distance = [float("inf")] * n
        # distance[src] = 0
        # # dp = [(0,src,0)]
        # dp = queue.PriorityQueue()
        # dp.put((0, src, K))
        # while not dp.empty():
        #     cost, start, stps = dp.get()
        #     data = flights_info[start]
        #     if start == dst:
        #         return cost
        #     if stps >= 0:
        #         for i, j in data:
        #             dp.put((cost + j, i, stps-1))

        ans = -1
        if not flights and src == dst:
            return ans
        flights_info = defaultdict(list)
        for u, v, w in flights:
            flights_info[u].append((v, w))

        dp = [(0, src, 0)]

        while dp:
            cost, start, stps = heapq.heappop(dp)
            data = flights_info[start]
            if start == dst:
                return cost
            if stps <= K+1:
                for i, j in data:
                    heapq.heappush(dp, (cost + j, i, stps + 1))

        return -1



if __name__ == "__main__":
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    # n = 5
    # edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    # src = 0
    # dst = 2
    # k = 2
    print(Solution().findCheapestPrice(n, edges, src, dst, k))