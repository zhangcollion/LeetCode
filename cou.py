from collections import  Counter
import re
class Solution:
    def maxDepth(self, s: str) -> int:
        max_res = 0
        if not s:
            return max_res
        if "(" not in s:
            return max_res
        getter = []
        ans = 0
        flag = 0
        s_list = list(s)
        re_s = re.findall("\(|\)", s)
        for loc , i in enumerate(re_s):
            if i is "(":
                if ans != 0 :
                    c = Counter(s_list[loc:])
                    ans += min(len(getter), c[")"])
                if ans > max_res:
                    max_res = ans
                getter.append(i)
                ans = 0
            if i is ")" and getter:
                getter = getter[:-1]
                ans += 1
        if ans > max_res:
            max_res = ans
        return max_res





if __name__ == "__main__":

    target = "(1+2)/(5+((4-9+8)*((1+8+(5*7)*4)/(7+9-5)))/(7/3-8-4-8))"
    print(Solution().maxDepth(target))