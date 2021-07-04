class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        time = []
        for d, s in zip(dist, speed):
            if d % s!= 0:
                time.append(d//s+1)
            else:
                time.append(d//s)
        time.sort()

        ans = 0
        while ans == 0 or (time and time[0]-ans >= 1 ):
            ans += 1
            time.pop(0)
        return ans