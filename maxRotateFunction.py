from typing import List
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        mul = list(range(0, len(A)))
        data = [mul[i] * A[i] for i in range(0, len(A))]
        all = sum(A)
        result = []
        result.append(sum(data))
        length = len(A)
        for k in range(0, len(A)-1):
            A[0], A[1:] = A[-1], A[:length - 1]
            result.append(result[k] - A[0] * mul[-1] + all - A[0])
        return (max(result))






if __name__=="__main__":
    A = [-8,5,-10,-5]
    print(Solution().maxRotateFunction(A))