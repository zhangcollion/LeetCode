class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        left = 0
        info_data = dict()
        ans = 0
        for right, value in enumerate(s):
            if value not in info_data:
                info_data[value] = 1
            else:
                info_data[value] += 1
            while (right-left+1) - max(info_data.values()) > k:
                info_data[s[left]] -= 1
                left += 1
            ans = max(ans, (right-left+1))
        return ans