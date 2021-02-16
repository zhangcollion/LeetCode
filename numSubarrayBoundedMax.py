from typing import List

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        if not A:
            return 0
        min_data = min(A)
        if min_data > R:
            return 0
        max_data = max(A)
        if max_data < L:
            return 0
        j = 0
        ans = 0
        max_data = 0
        while j < len(A):
            if A[j] > max_data:
                max_data = A[j]
            if L <= max_data <= R:
                ans += 1
                j += 1
            else:
                max_data = 0
                if j + 1 < len(A):
                    j += 1
                else:
                    break
        return ans



if __name__ == "__main__":
    W = [2, 1, 4, 3, 1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1]
    L = 2
    R = 3
    print(Solution().numSubarrayBoundedMax(W, L, R))