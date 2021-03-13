import collections
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = collections.defaultdict()
        def get_ans(str_in, wordDict):
            if str_in in seen:
                return seen[str_in]
            if not str_in:
                return True
            for idx in range(len(str_in), -1, -1):
                if str_in[:idx + 1] in wordDict:
                    ans = get_ans(str_in[idx + 1:], wordDict)
                    if ans:
                        return ans
            seen[str_in] = False
            return False

        return get_ans(s, wordDict)
