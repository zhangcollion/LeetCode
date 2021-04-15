class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a <=2 and b <= 2:
            return "a"*a+"b"*b
        ans = ""
        if a > b:
            ref = ["aa"] * (a//2)
            if a%2 > 0:
                ref.append("a"*(a%2))
            need = "b"
            left = b
        if a <= b:
            ref = ["bb"] * (b//2)
            if b%2 > 0:
                ref.append("b"*(b%2))
            need = "a"
            left = a
        n = len(ref) 
        ans = []
        if n > left:
            ans = [need] * left
        else:
            ans = [need] * n
        left = left - n
        i = 0
        while left > 0:
            ans[i] += need
            i += 1
            left -= 1
        n = min(len(ref), len(ans))
        res = ""
        for i in range(n):
            res += ref[i]
            res += ans[i]
        if len(ref) > n:
            res += ref[-1]
        if len(ans) > n:
            res += ans[-1]
        return res

        

