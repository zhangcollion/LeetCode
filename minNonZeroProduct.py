class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p <= 1:
            return 1
        n = 2**p
        tmp = 10**9+7
        ans = 1 * pow((n-2), ((n-1)//2),tmp)*(n-1)
        return mod(ans, tmp)