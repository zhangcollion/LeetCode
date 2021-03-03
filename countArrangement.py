class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1:
            return 1

        self.ref = list(range(1, n + 1))
        self.n = n
        self.ans = 0
        self.dfs([], 0)
        return (self.ans)


    def dfs(self, res, idx):
        if len(res) == self.n:
            self.ans += 1
            return
        for j in range(0, len(self.ref)):
            k = len(res)
            i = self.ref[j]
            if (not ((k + 1) % i) or not ((i) % (k + 1)) ):
                if not res:
                    self.dfs(res + [i], 0)
                else:
                    if i not in res:
                        self.dfs(res + [i], 0)

if __name__=="__main__":
    n = 15
    print(Solution().countArrangement(n))
