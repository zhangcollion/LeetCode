class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            nums.sort()
            n = len(nums)//2
            for i in range(n):
                tmp = nums.pop()
                nums.insert(n-i-1, tmp)