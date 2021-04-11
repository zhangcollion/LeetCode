from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        stack = []
        ans = -1
        for i in nums:
            if i in stack:
                ans =  max(ans, sum(stack))
                idx = stack.index(i)
                if idx == len(stack) - 1:
                    stack = []
                else:
                    stack = stack[idx+1:]
                stack.append(i)
            else:
                stack.append(i)

        return max(ans, sum(stack))


if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    heights = [5,2,1,2,5,2,1,2,5]
    print(Solution().maximumUniqueSubarray(heights))