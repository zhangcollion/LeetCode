class Solution:
    def makeStringSorted(self, s: str) -> int:
        ans_s = sorted(s)
        ans_s = "".join(ans_s)
        ans = 0
        while s != ans_s:
            s = list(s)
            for i in range(len(s)-1, 0, -1):
                if s[i] < s[i-1]:
                    ref = i
                    break
            ref_data = s[ref-1]
            for j in range(ref, len(s)):
                if s[j] < ref_data:
                    ref_j = j
                else:
                    break
            s[ref-1], s[ref_j] = s[ref_j], s[ref-1]
            tmp_s = s[ref:]
            s[ref:] = tmp_s[-1::-1]
            s = "".join(s)
            ans += 1

        return ans%(10**9+7)




if __name__ == "__main__":
    s = "cdbea"
    print(Solution().makeStringSorted(s))