class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = len(piles)//3
        min_data = sum(piles[left::2])
        return min_data