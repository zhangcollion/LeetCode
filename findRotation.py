import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        mat = np.array(mat)
        tmp = mat.copy()
        target = np.array(target)
        for i in range(4):
            for row in range(n):
                mat[row, :] =  tmp[:,row][-1::-1]
            flag = 0
            for row in range(n):
                for col in range(n):
                    if mat[row][col] != target[row][col]:
                        flag = 1
                        break
            if 0 == flag:
                return True
            tmp = mat.copy()
        return False