class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans = ""
        for i, v in enumerate(words):
            ans += v
            if ans == s:
                return True
            if len(ans) > len(s):
                return False
        return False   