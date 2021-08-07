class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        ans = 0 
        ref_data = "0" * n
        for i in range(n):
            if target[i] == ref_data[i]:
                continue
            else:
                ans += 1
                if target[i] == "0":
                    ref_data = "0"*n
                else: 
                    ref_data = "1"*n
        return ans