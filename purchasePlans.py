from typing import  List
from collections import Counter
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        info = Counter(nums)
        info = sorted(info.keys())
        n = len(info)
        for i in range(0, n-1):
            for j in range(1, n):
                if info[] + info[] >
        ans = 0
        return ans

    if __name__ == "__main__":
        nums = [2, 2, 1, 9]
        target = 10
        print(Solution().purchasePlans(nums, target))