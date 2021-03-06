class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        if not points:
            return -1
        info = defaultdict()
        for i, v in enumerate(points):
            m, n = v
            if m == x or n == y:
                info[i] = abs(m - x) + abs(n - y)
        if not info:
            return -1
        min_ans = min(info.values())
        for i in info.keys():
            if info[i] == min_ans:
                return i

        return -1