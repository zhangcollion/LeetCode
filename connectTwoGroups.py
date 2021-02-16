from typing import *
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        if not cost:
            return 0
        A_num = len(cost)
        B_num = len(cost[0])
        flag_A = [0]*A_num
        flag_B = [0]*B_num
        res = 0
        for i, data in enumerate(cost):
            min_data = min(data)
            res += min_data
            idx = data.index(min_data)
            flag_B[idx] = 1
            flag_A[i] = 1
        if 0 in flag_B:
            idx_flag = flag_B.index(0)
            for i in idx_flag:
                data = [ele[i] for ele in cost]
                min_data = min(data)
                res += min_data
                flag_B[i] = 1
        else:
            return res
