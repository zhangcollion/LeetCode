from collections import defaultdict


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if not expression:
            return expression
        info = defaultdict(list)
        tmp = ""
        ans = []
        for i in expression:
            if i == "/":
                ans.append(tmp)
                tmp = ""
            else:
                if i in ["+", "-"]:
                    if tmp:
                        ans.append(tmp)
                        tmp = i
                    else:
                        tmp = i
                else:
                    tmp += i
        ans.append(tmp)
        for i in range(0, len(ans), 2):
            if int(ans[i + 1]) not in info.keys():
                info[int(ans[i + 1])] = int(ans[i])
            else:
                info[int(ans[i + 1])] = info[int(ans[i + 1])] + int(ans[i])

        mom = list(info.keys())
        son = list(info.values())
        ans = 1
        for i in mom:
            ans *= i
        tmp = 0
        for i in range(len(son)):
            tmp += son[i] * ans // mom[i]
        from fractions import Fraction
        f = Fraction(tmp, ans)
        ans = str(f._numerator) + "/" + str(f._denominator)
        return ans


if __name__ == "__main__":
    s = "-5/2+10/3+7/9"
    print(Solution().fractionAddition(s))
