class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = set()
        ref = list(str(i) for i in range(10))
        res = ""
        for i in word:
            if i in ref:
                if res:
                    res += i
                else:
                    if i == "0":
                        continue
                    else:
                        res += i
            else:
                if res:
                    ans.add(res)
                    res = ""
        return len(res)