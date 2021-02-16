from typing import List


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        if not s:
            return ans

        def get_ans(n):
            data = 0
            for i in range(1, n + 1):
                data += i

            return data

        i = 0
        s_info = list(s)
        while i < len(s_info) :
            j = i + 1
            while j < len(s_info):
                if s_info[j] != s_info[i]:
                    break
                else:
                    j += 1
            n = len(s_info[i:j])
            ans += get_ans(n)
            i = j

        return ans%(pow(10, 9)+7)


if __name__ == "__main__":
    s = "abbcccaa"
    print(5000050000%(pow(10, 9)+7))
    print(Solution().countHomogenous(s))
