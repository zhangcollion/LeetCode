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
                if  i in ["+","-"]:
                    if tmp:
                        ans.append(tmp)
                        tmp = i
                    else:
                        tmp = i
                else:
                    tmp += i
        ans.append(tmp)
        print(ans)
        for i in range(0, len(ans), 2):
            info[int(ans[i + 1])].append(int(ans[i]))

        info_dict = defaultdict(list)
        for i in info.keys():
            data = sum(info[i])
            if data != 0:
                info_dict[i] = data

        mom = list(info_dict.keys())
        son = list(info_dict.values())

        ans = 1
        for i in mom:
            ans *= i
        tmp = 0
        for i in range(len(son)):
            tmp += son[i] * ans // mom[i]
        # print(ans, tmp)
        from fractions import Fraction
        f = Fraction(tmp, ans)
        ans = str(f._numerator) + "/" + str(f._denominator)
        return ans



if __name__ == "__main__":
    s = "-5/2+10/3+7/9"
    print(Solution().fractionAddition(s))
