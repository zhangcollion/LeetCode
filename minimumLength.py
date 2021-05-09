class Solution:
    def minimumLength(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = len(s) - 1

        while left < right and  s[left] == s[right]:
                while s[left+1] == s[left] and left+1 < right:
                    left += 1
                while s[right-1] == s[right] and left < right-1:
                    right -= 1
                left += 1
                right -= 1

        return right - left + 1