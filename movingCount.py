class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k <= 0:
            return 1
        self.seen = []
        self.K  = k
        self.get_ans(0, 0, m, n)
        print(self.seen)
        return len(self.seen)

    def isvalid(self,r, c, k):
        sum_data = 0

        while r > 9:
            r, d = divmod(r, 10)
            sum_data += d
        sum_data += r

        while c > 9:
            c, d = divmod(c, 10)
            sum_data += d
        sum_data += c

        if sum_data <= k:
            return True
        else:
            return False
    def get_ans(self,i, j, m, n):
        for k, v in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
            if 0 <= k < m and 0 <= v < n and (k ,v) not in self.seen:
                if self.isvalid(k,v,self.K):
                    self.seen.append((k,v))
                    self.get_ans(k, v, m,n)


if __name__ == "__main__":
    m = 3
    n = 1
    k = 0
    print(divmod(521, 10))
    print(Solution().movingCount(m, n, k))