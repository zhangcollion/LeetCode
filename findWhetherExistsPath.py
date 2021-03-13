class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if not graph:
            return False
        graph = set(graph)
        info = collections.defaultdict(list)
        for i in graph:
            a, b = i
            if a == b:
                continue
            else:
                info[a].append(b)

        def dfs(info, left, end, seen):
            if left == end:
                return True
            for i in info[left]:
                ans = dfs(info, i, end, seen + [i])
                if ans:
                    return True
            return False

        seen = [start]
        return dfs(info, start, target, seen)
