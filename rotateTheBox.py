class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n_rows = len(box)
        n_cols = len(box[0])
        ans = [["." for i in range(n_rows)] for i in range(n_cols)]
        for box_idx in range(n_rows):
            box_ele = box[box_idx]
            for i in range(n_cols - 2, -1, -1):
                next_i = i + 1
                if box_ele[i] == "#":
                    while next_i <= n_cols - 1:
                        if box_ele[next_i] == ".":
                            box_ele[next_i - 1] = "."
                            box_ele[next_i] = "#"
                            next_i += 1
                        else:
                            break
            for k in range(n_cols):
                ans[k][n_rows - box_idx - 1] = box_ele[k]

        return ans