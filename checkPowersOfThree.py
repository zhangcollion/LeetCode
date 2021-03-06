class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        idx = 0
        for i in range(1, n):
            if pow(3, i) >= n:
                idx = i
                break
        ref = list(range(idx+1))
        self.re = []
        ans = self.get_ans(ref, n)
        return ans

    def get_ans(self, ref, n):
        if n == 0:
            return True
        for i in range(len(ref)):
            if pow(3, ref[i]) <= n and i < len(ref)-1:
                ans = self.get_ans(ref[i+1:], n - pow(3,ref[i]))
                if ans:
                    return ans
            if pow(3, ref[i]) == n :
                return True
        return False


if __name__== "__main__":
    n = 27
    print(Solution().checkPowersOfThree(n))

