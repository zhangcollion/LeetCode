from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(0, length):
            sum_data = 0
            for j in range(i, length):
                sum_data += nums[j]
                if k != 0:
                    if sum_data%k == 0  and j-i >= 1:
                        return True
                if k == 0 :
                    check_data = list(set(nums[i:j+1]))
                    if check_data[0] == 0 and j-i >= 1 and len(check_data)==1:
                        return True
        return False