from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        data = ["(", ")"]
        re = []
        def get_parenthesis(tmp):
            if len(tmp) == 2*n and valid(tmp):
                re.append(tmp)
                return
            if len(tmp) > 2*n:
                return
            for i in range(0, len(data)):
                get_parenthesis(tmp + [data[i]])

        def valid(parenthesis):
            left = 0
            for i in range(0, len(parenthesis)):
                if parenthesis[i] == "(":
                    left += 1
                if parenthesis[i] == ")" :
                    if left > 0:
                        left -= 1
                    else:
                        return False
            if left == 0:
                return True

        get_parenthesis([])
        res = []
        for ele in re:
            res.append("".join(ele))
        return res


if __name__ == "__main__":
    nums = 3
    print(Solution().generateParenthesis(nums))
    num = [1,2]
    re = "!sdaasdsaa"
    print(re.rfind("a"))