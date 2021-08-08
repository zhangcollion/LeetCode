class Solution:
    def minSwaps(self, s: str) -> int:
        ans = []
        for i in s:
            if not ans:
                ans.append(i)
                continue
            if ans[-1] == "[" and i == "]":
                ans.pop(-1)
            else:
                ans.append(i)
        data = list("".join(ans))
        res = 0
        if len(data)==0:
            return 0
        left = len(data)//2 
        if left % 2 == 0: 
            return left//2
        else:
            return left//2 + 1
        

            
                