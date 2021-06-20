class Solution:
    def largestOddNumber(self, num: str) -> str:
        ref = ["1", "3", "5", "7", "9"]
        ans = ""
        idx = 0
        for i in range(len(num)-1, -1,-1):
            if num[i] in ref:
                idx = i
                break
        if idx == 0:
            if num[:idx+1] in ref:
                return num[:idx+1]
            else:
                return ""
        return num[:idx+1]