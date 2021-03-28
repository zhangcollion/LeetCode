class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = [0] * n
        cnt = 0

        def not_valid(arr, perm):
            for i in range(n):
                if arr[i] != perm[i]:
                    return True
            return False
        goal = perm.copy()
        while not_valid(arr, goal):
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            perm = arr.copy()
            cnt += 1

        return cnt


if __name__=="__main__":
    n = 4
    print(Solution().reinitializePermutation(n))