from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for idx, val in enumerate(asteroids):
            if not stack or stack[-1] < 0:
                stack.append(val)
                continue
            if (stack[-1] < 0 and val < 0) or (stack[-1] >= 0 and val >= 0):
                stack.append(val)
                continue
            flag = 0
            while stack:
                if stack[-1] * val < 0:
                    if abs(stack[-1]) < abs(val):
                        flag = 1
                        stack.pop(-1)
                    elif abs(stack[-1]) == abs(val) :
                        flag = 0
                        stack.pop(-1)
                        break
                    else:
                        flag = 0
                        break
                else:
                    flag = 1
                    break
            if 1 == flag:
                stack.append(val)
        return stack



if __name__ == "__main__":
    s =[10,5,-5,-8,-8,-10]
    print(Solution().asteroidCollision(s))