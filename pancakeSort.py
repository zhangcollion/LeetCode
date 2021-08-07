class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        n = len(A)
        while n :
            idx = A.index(n)
            if idx == 0:
                A[:n] = A[n-1::-1]
                ans.append(n)
            elif idx != n-1:
                ans.append(idx+1)
                A[:idx+1] = A[idx::-1]
                A[:n] = A[n-1::-1]
                ans.append(n)  
            n -= 1

        return ans