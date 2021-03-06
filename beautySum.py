from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        if len(s) < 3:
            return 0
        n = len(s)
        ref = list(range(2, n ))
        ans = 0
        while ref:
            left = 0
            right = ref.pop()
            info = Counter(s[left:right+1])
            sorted(info.items(), key=lambda item : item[1])
            while right < n:




