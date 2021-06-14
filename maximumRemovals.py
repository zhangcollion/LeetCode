from typing import List
from collections import Counter
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def is_valid(ref):
            ref = set(removable[:ref])
            data = ""
            for i in range(len(s)):
                if i not in ref:
                    data += s[i]
            for i in p:
                try :
                    index = data.index(i)
                    data = data[index+1:]
                except:
                    return False
            return True

        
        
        n = len(removable)
        right = n
        left = 0
        while left <= right:
            mid = (right + left)//2
            # print(mid)
            if is_valid(mid):
                left = mid+1
            else:
                right = mid-1
        
        return min(mid, left, right)