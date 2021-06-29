class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        left_num = len(num) - k
        stack = []
        for i in num:
            while k > 0 and stack and int(stack[-1]) > int(i):
                stack.pop()
                k -= 1

            stack.append(str(i))
        
        ans = "".join(stack[:left_num])
        if ans:
            return str(int(ans))
        else:
            return "0"
        
