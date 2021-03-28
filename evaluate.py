from collections import defaultdict
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        if not s:
            return s
        if "(" not in s or ")" not in s:
            return s
        info = defaultdict()
        for ele in knowledge:
            a, b = ele
            info[a] = b
        stack = []
        ans = ""
        for i in s:
            if i == "(":
                if stack:
                    tmp = "".join(stack)
                    ans += tmp
                    stack.clear()
                stack.append(i)
            elif i == ")":
                tmp = "".join(stack[1:])
                if tmp in info.keys():
                    ans += info[tmp]
                else:
                    ans += "?"
                stack.clear()
            else:
                stack.append(i)
        if stack:
            tmp = "".join(stack)
            ans += tmp
        return ans


if __name__ == "__main__":
    s = "(a)(a)(a)aaa"
    knowledge = [["a", "yes"]]
    print(Solution().evaluate(s, knowledge))
