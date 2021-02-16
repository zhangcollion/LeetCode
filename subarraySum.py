from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        appear_data = {0:1}
        pre_data = 0
        count = 0
        for ele in nums:
            pre_data += ele
            old_exit = pre_data - k
            if old_exit in appear_data:
                count += appear_data[old_exit]
            appear_data[pre_data] = appear_data.get(pre_data, 0) + 1

        return count


if __name__=="__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))


    def b(a, *x,**l):
        print(x)
        print(l)
    b(1, 2, 3, 4, k=2333)