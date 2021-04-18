class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:

        s = 0
        for num in arr2:
            s ^= num
        ans = 0
        for num in arr1:
            ans ^= (num & s)
        return ans