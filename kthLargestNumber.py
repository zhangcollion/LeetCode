class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        data = [int(i) for i in nums]
        data.sort()
        return str(data[len(nums)-k])