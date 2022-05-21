from Typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if len(seq) == 0:
            return []
        ans = []
        d = 0
        for c in seq:
            if c is "(":
                d += 1
                ans.append(d%2)
            else:
                d -= 1
                ans.append(d%2)
        return ans
