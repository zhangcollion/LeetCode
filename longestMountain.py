from typing import *
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        left = [0]*n
        for i in range(1, n):
            left[i] = (left[i-1]+1 if A[i]>A[i-1] else 0)

        right = [0]*n
        for i in range(n-2, -1, -1):
            right[i] = (right[i+1]+1 if A[i+1]<A[i] else 0)

        res = 0
        for i in range(n):
            if left[i]>0 and right[i]>0:
                res = max((left[i]+right[i]+1), res)


        return res



if __name__ == "__main__":
    nums = [2,1,4,7,3,2,5]
    print(Solution().longestMountain(nums))
