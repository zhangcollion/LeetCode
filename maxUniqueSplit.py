from typing import *


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        if not s:
            return res
        ref = []
        data = ""
        for ele in s:
            data += ele
            if data not in ref:
                res += 1
                ref.append(data)
                data = ""
            else:
                data += ele
        ref = []
        data = ""
        for ele in s:
            data += ele
            if data not in ref:
                ref.append(data)
                data = ""
            else:
                if ref[-1] == data:
                    ref[-1] = data + ele
        res3 = len(ref)
        res2 = 0
        s_data = s[::-1]
        ref = []
        data = ""
        for ele in s_data:
            data += ele
            if data not in ref:
                res2 += 1
                ref.append(data)
                data = ""
            else:
                if ref[-1] == data:
                    ref[-1] = data + ele
        return max(res3, res, res2)

if __name__ == "__main__":
    #s = "ababccc"
    # s = "gpaccacseleac"
    s = "mibaiiaecmcbj"
    print(Solution().maxUniqueSplit(s))
