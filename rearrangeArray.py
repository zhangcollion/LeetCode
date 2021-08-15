class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def is_valid(data):
            for i in range(1, len(data)-1):
                if data[i] == (data[i-1]+data[i+1])/2:
                    return True
            return False
        from random import shuffle
        while is_valid(nums):
            shuffle(nums)
        return nums