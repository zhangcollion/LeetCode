from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda balloon: balloon[1])
        ans = 1
        arrow_left, arrow_right = points[0]
        for point_data in points:
            a, b = point_data
            if a > arrow_right or b < arrow_left:
                arrow_left, arrow_right = point_data
                ans += 1
            else:
                arrow_left = max(arrow_left, a)
                arrow_right = min(b, arrow_right)
                arrow_right = min(b, arrow_right)
        return ans



if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    heights = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(Solution().findMinArrowShots(heights))
