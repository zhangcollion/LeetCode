from typing import List
from collections import Counter

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        cnt = Counter(nums)
        cnt_keys =  list(cnt.keys())
        while True:
            if len(cnt_keys) == 1:
                break
            cnt_keys.sort()
            min_data = cnt_keys[0]
            max_data = cnt_keys[-1]
            if cnt[min_data] <= cnt[max_data]:
                ans += (cnt_keys[1] - min_data) * cnt[min_data]
                cnt[cnt_keys[1] ] += cnt[cnt_keys[0]]
                del cnt[cnt_keys[0]]
                cnt_keys.pop(0)
            else:
                ans += cnt[max_data]*(max_data- cnt_keys[-2])
                cnt[cnt_keys[-2]] += cnt[cnt_keys[-1]]
                del cnt[cnt_keys[-1]]
                cnt_keys.pop(len(cnt_keys)-1)
            # cnt_keys = list(cnt.keys())
        return ans

if __name__== "__main__":
    in_data = [30,55]
    print(Solution().minMoves2(in_data))