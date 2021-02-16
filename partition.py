from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return list()
        self.data = []
        self.re = []
        self.s = s
        self.ele = []
        s_input = list(s)
        start_idx = 0
        self.get_next(s_input, start_idx )
        return self.re

    def get_next(self, s, idx):
        if len(self.data) == 1 | self.is_back(self.data):
            self.ele.extend(self.data)
            self.data = []
        if idx == len(self.s):
            tmp = ""
            for i in self.ele:
                tmp += "".join(i)
            if tmp == self.s:
                self.re.append(self.ele)
                return
        for i, e in enumerate(s[idx:]):
             self.data.append(e)
             self.get_next(s, idx+1)


    def is_back(self, str_in):
        str_back = "".join(str_in[::-1])
        str_com = "".join(str_in)
        if str_back == str_com:
            return True
        else:
            return False


if __name__=="__main__":
    # candidates = [2, 3, 6, 7]
    heights = "aab"
    print(Solution().partition(heights))

