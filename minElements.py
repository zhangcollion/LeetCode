from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        data = sum(nums)
        if data == goal:
            return 0

        deta = goal - data
        ref = min(abs(deta), abs(limit))
        ref_data = list(range(-ref, ref + 1))
        if deta < 0:
            flag = -1
            ref_data.sort()
        else:
            flag = 1
            ref_data.sort(reverse=True)

        def get_ans(target, ref_data, cnt, flag):
            if target in ref_data:
                return  cnt + 1
            if target == 0:
                return cnt
            if flag == -1:
                if target > 0:
                    return
            if flag == 1:
                if target < 0:
                    return
            for i in ref_data:
                ans = get_ans(target - i, ref_data, cnt + 1, flag)
                if ans > 0:
                    return ans
            return -1
        add = deta//ref_data[0]
        left = deta%ref_data[0]
        if left == 0:
            return add
        ans = get_ans(left, ref_data, add, flag)
        return  ans


if __name__=="__main__":
    nums = [1,-10,9,1]
    limit = 100
    goal = 0
    # nums = [2, 2, 2, 5, 1, -2]
    # limit = 5
    # goal= -126614243
    print(Solution().minElements(nums, limit, goal))