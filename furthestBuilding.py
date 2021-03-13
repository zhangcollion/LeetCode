from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0
        ans = [0]
        for i in range(len(heights)-1):
            if heights[i+1] > heights[i]:
                ans.append(heights[i+1]-heights[i])
            else:
                ans.append(0)
        non_num = ans.count(0)
        if len(ans) - non_num <= ladders or sum(ans) <= bricks:
            return len(ans) - 1

        def is_valid(loc, ans, brick_num , ladder_num):
            ref = ans[0:loc]
            zero = ref.count(0)
            non_zero = len(ref) - zero
            if sum(ref) <= brick_num or non_zero <= ladder_num:
                return True
            ref.sort(reverse=True)
            left_ref = ref[ladder_num:]
            if sum(left_ref) <= brick_num:
                return True
            return False

        right = len(heights) - 1
        left = 0
        n = (right + left)//2
        while n < right:
            if is_valid(n, ans, bricks, ladders):
                left = n+1
                n = (left+right)//2
            else:
                right = n
                n = (left+right)//2
        return n-1


if __name__=="__main__":
    heights = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2
    print(Solution().furthestBuilding(heights, bricks, ladders))