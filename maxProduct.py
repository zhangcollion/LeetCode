class Solution:
    def maxProduct(self, words: List[str]) -> int:
        tmp_data = [0] * len(words)
        for i in range(len(words)):
            code = 0
            for c in words[i] :
                code |= 1<<(ord(c)-ord('a'))
            tmp_data[i] = code
        ans = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if not (tmp_data[i] & tmp_data[j]):
                    ans = max(ans, len(words[i])*len(words[j]))

        return ans


