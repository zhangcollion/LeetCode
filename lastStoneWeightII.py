from typing import List
from functools import lru_cache
from collections import defaultdict
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.ans = float("inf")

        @lru_cache(None)
        def backtrack(i, c):
            if i == len(stones):
                self.ans = min(self.ans, abs(c))
                return
            backtrack(i + 1, c + stones[i])
            backtrack(i + 1, c - stones[i])

        backtrack(0, 0)
        backtrack.cache_clear()

        return self.ans

        # if not stones:
        #     return 0
        #
        # while len(stones) > 1:
        #     stones.sort()
        #     a = stones.pop(-1)
        #     b = stones.pop(-1)
        #     stones.append(a-b)
        #
        # if stones:
        #     return stones[0]
        # return 0

if __name__=="__main__":
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeightII(stones))
