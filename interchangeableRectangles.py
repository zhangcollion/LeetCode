class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        tmp_ans = []
        for data in  rectangles:
            m, n = data
            tmp_ans.append(m/n)
            
        info_data = Counter(tmp_ans)
        ans = 0
        for i in info_data:
            if info_data[i]  >= 2:     
                tmp = 0
                for j in range(1, info_data[i]):
                    tmp += j
            else:
                tmp = 0
            ans += tmp
            
        return ans