class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ["a"]*n
        num = 0
        for i in ans:
            num += ord(i)-96
        i = n - 1
        while num != k:
            if k - num >= 26:
                num += 25
                ans[i] = "z"
                i -= 1
            else:
                ans[i] = chr(k - num + 97)
                num += k - num
        return "".join(ans)