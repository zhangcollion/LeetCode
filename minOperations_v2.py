from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        count = 0
        diff = sum1 - sum2

        if diff == 0:
            return 0

        left = len(nums1) - 1
        right = 0

        while left >= 0 or right < len(nums2):
            if left >= 0:
                left_diff = nums1[left] - 1
            else:
                left_diff = 0
            if right < len(nums2):
                right_diff = 6 - nums2[right]
            else:
                right_diff = 0

            if left_diff == 0 and right_diff == 0:
                break

            if left_diff > right_diff:
                diff -= left_diff
                left -= 1
            else:
                diff -= right_diff
                right += 1

            count += 1

            if diff == 0:
                break


        if diff <= 0:
            return count
        return -1


if __name__ == "__main__":
    nums1 = [1, 5, 5, 2, 1, 1, 1, 1, 4, 4, 4, 1, 5, 2, 2, 4, 6, 5, 1, 5, 3, 5, 6, 2, 3, 1, 5, 4, 4, 1, 2, 4, 1, 1, 6, 3,
             6, 4, 4, 4, 3, 5, 5, 5, 2, 6, 4, 2, 5, 4, 2, 6, 3, 4, 6, 1, 5, 3, 2, 3, 5, 2, 1, 3, 2, 4, 4, 4, 5, 3, 5, 5,
             4, 1, 1, 6, 5, 6, 3, 5, 3, 6, 5, 6, 5, 4, 4, 4, 5, 6, 6, 6, 4, 2, 4, 6, 1, 2, 1, 5, 3, 4, 5, 5, 6, 6, 1, 4,
             3, 1, 5, 3, 4, 1, 2, 1, 4, 4, 5, 6, 5, 3, 1, 5, 1, 3, 3, 6, 5, 3, 5, 6, 2, 6, 3, 1, 2, 3, 3, 1, 1, 4, 3, 2,
             6, 6, 2, 1, 2, 4, 3, 5, 5, 4, 3, 1, 1, 5, 2, 5, 1, 4, 5, 6, 4, 5, 2, 1, 2, 5, 3, 2, 6, 3, 4, 3, 4, 5, 4, 6,
             3, 4, 4, 3, 3, 4, 2, 2, 6, 2, 6, 3, 1, 1, 5, 3, 1, 1, 4, 2, 5, 5, 5, 4, 3, 6, 5, 5, 5, 1, 1, 3, 6, 2, 3, 6,
             3, 4, 2, 5, 4, 4, 3, 5, 6, 4, 3, 5, 1, 1, 3, 3, 1, 1, 6, 4, 6, 2, 1, 4, 3, 5, 5]
    nums2 = [1, 2, 5, 4, 3, 3, 5, 1, 1, 6, 2, 5, 4, 4, 5, 6, 6, 4, 2, 5, 6, 2, 3, 4, 5, 2, 4, 4, 3, 6, 6, 5, 4, 1, 2, 1,
             2, 3,
             3, 2, 6, 1, 1, 1, 1, 3, 5, 6, 2, 1, 1, 1, 4, 6, 5]
    # nums2 = [1]
    print(Solution().minOperations(nums1, nums2))
