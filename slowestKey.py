from typing import *
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if not releaseTimes or not keysPressed:
            return "None"
        res = [0]*len(releaseTimes)
        for i in range(len(releaseTimes)):
            if i == 0 :
                res[i] = (releaseTimes[i])
            else:
                res[i] = (releaseTimes[i]-releaseTimes[i-1])
        ref = []
        for i, val in enumerate(res):
            if val == max(res):
                ref.append(i)
        ans = "a"
        for i in ref:
            ans = max(keysPressed[i], ans)
        return ans


if __name__ == "__main__":
    releaseTimes = [12,23,36,46,62]
    keysPressed = "spuda"
    print(Solution().slowestKey(releaseTimes, keysPressed))