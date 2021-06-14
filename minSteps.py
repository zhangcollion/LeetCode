from typing import List
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_info = Counter(s)
        t_info = Counter(t)
        
        ans = 0
        for i in s_info.keys():
            if t_info[i] < s_info[i]:
                ans += s_info[i] - t_info[i]
            
        return ans