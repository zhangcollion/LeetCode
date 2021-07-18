class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        seen  = set()
        for i in range(len(s)-2):
            ref = s[i]
            if ref not in seen:
                seen.add(ref)
                left = set()
                for j in range(i+1, len(s)-1):
                    if s[j] not in left:
                        left.add(s[j])
                        tmp = ref+s[j]
                        if ref in set(s[j+1:]):
                            if not ans or tmp not in ans:
                                ans.add(tmp+ref)
        # print(ans)
        return len(ans)