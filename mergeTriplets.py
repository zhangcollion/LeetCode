from typing import List
from collections import Counter
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a, b, c = 0, 0, 0
        for i, j , k in triplets:
            if i <= x and j <= y and k <= z:
                a = max(i, a)
                b = max(j, b)
                c = max(k, c)

        return (a, b, c) == (x, y, z)