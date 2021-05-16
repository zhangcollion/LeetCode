class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        res = n + 1
        ref_data = ["01", "10"]
        
        for i in range(0, 2):  
            s1 = ref_data[i] * (n // 2)
            if n % 2 == 1:
                s1 += str(i)

            n01, n10 = 0, 0
            for x, y in zip(s, s1):
                if x == '1' and y == '0':
                    n10 += 1
                elif x == '0' and y == '1':
                    n01 += 1
            if n10 == n01:
                res = min(res, n10)
            
        if res == n+1:
            return -1
        return res