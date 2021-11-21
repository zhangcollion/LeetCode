class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = 0
        ans = 0 
        left_capacity = capacity
        while i < len(plants):
            if plants[i] > left_capacity:
                ans += i + i + 1
                left_capacity = capacity
                left_capacity -= plants[i] 
                i += 1
                continue
            else:
                ans += 1
                left_capacity -= plants[i] 
                i += 1
        return ans