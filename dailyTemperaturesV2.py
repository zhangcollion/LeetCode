class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =  [0] * len(temperatures)
        tmp_data = []
        for loc, temp in enumerate(temperatures):
            if not temp :
                tmp_data.append(loc)
                continue
            else:
                while tmp_data and temperatures[tmp_data[-1]] < temp:
                    idx = tmp_data.pop()
                    ans[idx] = loc-idx
                tmp_data.append(loc)
        return ans
