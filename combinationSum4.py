from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        self.dfs(nums, [], target)
        return self.ans

    def dfs(self, s, path, target):
        print(path)
        if sum(path) > target:
            return
        if sum(path) == target:
            self.ans += 1
            return

        for i in range(len(s)):
            print(s[:])
            print(s[i])
            self.dfs(s[:], path + (s[i:i+1]), target)




if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 32
    print(Solution().combinationSum4(nums, target))