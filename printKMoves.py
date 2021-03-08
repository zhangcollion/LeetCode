from typing import List
class Solution:
    def printKMoves(self, K: int) -> List[str]:
        if 0 == K:
            return ["R"]

        direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        info = {0: "L", 1: "U", 2: "R", 3: "D"}
        start_point = (0, 0)
        toward_idx = 2
        seen = []
        min_row = float("inf")
        min_cols = float("inf")
        while K > 0:
            steps = direction[toward_idx]
            next_point = (start_point[0] + steps[0], start_point[1] + steps[1])
            min_row = min(min_row, next_point[0])
            min_cols = min(min_cols, next_point[1])
            if not seen or next_point not in seen:
                seen.append(next_point)
                toward_idx = (toward_idx + 1) % 4
            else:
                seen.remove(next_point)
                toward_idx = (toward_idx - 1) % 4

            start_point = next_point
            K -= 1
        next_point = (start_point[0] + direction[toward_idx][0], start_point[1] + direction[toward_idx][1])
        min_row = min(min_row, next_point[0])
        min_cols = min(min_cols, next_point[1])
        towards = info[toward_idx]
        base_x = abs(min_row)
        base_y = abs(min_cols)
        ans = []
        max_row = float("-inf")
        max_col = float("-inf")
        for ele in seen:
            i, j = ele
            ans.append((i + base_x, j + base_y))
            max_row = max(max_row, (i + base_x))
            max_col = max(max_col, (j + base_y))

        direc_loc = (next_point[0] + base_x, next_point[1] + base_y)
        max_row = max(max_row, direc_loc[0]  )
        max_col = max(max_col, direc_loc[1]  )
        res = [["_" for j in range(max_col + 1)] for i in range(max_row + 1)]
        for i, j in ans:
            res[i][j] = "X"
        i, j = direc_loc
        res[i][j] = towards
        ans = []
        for i in range(len(res) - 1, -1, -1):
            tmp = "".join(res[i])
            ans.append(tmp)
        return ans


if __name__=="__main__":
    K = 1
    print(Solution().printKMoves(K))
