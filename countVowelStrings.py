class Solution:
    def countVowelStrings(self, n: int) -> int:
        count = [1]*5
        if n == 1:
            return sum(count)
        for j in range(1,n):
            for i in range(1,5):
                count[i] = count[i-1] + count[i]         
        return sum(count)