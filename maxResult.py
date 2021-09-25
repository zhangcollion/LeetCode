from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        import numpy as np
        ans = nums[0]
        for i in range(1, len(nums), k):
            if i + k  >= len(nums):
                end = len(nums)+1
                tmp_data = nums[i:end]
                tmp_data = np.array(tmp_data)
                tmp_loc = np.where(tmp_data > 0)
                if tmp_data[tmp_loc]:
                    ans += sum(tmp_data[tmp_loc])
                    if len(tmp_data) - 1 not in tmp_loc:
                        ans += nums[-1]
                else:
                    ans += nums[-1]
            else:
                end = i + k
                tmp_data = nums[i:end]
                tmp_data = np.array(tmp_data)
                tmp_loc = np.where(tmp_data > 0)
                if tmp_data[tmp_loc]:
                    print(tmp_data[tmp_loc])
                    ans += sum(tmp_data[tmp_loc])
                else:
                    ans += max(tmp_data)

        return ans



if __name__ == "__main__":
    nums = [100,-1,-100,-1,100]
    k = 2
    print(Solution().maxResult(nums, k))