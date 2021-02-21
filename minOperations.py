from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if not boxes:
            return []

        ans = []

            
        for i, ref in enumerate(boxes):
            re = 0
            for j, value in enumerate(boxes):
                if value == "0":
                    re += abs(j-i)

            ans.append(re)
        return ans