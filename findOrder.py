class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(0, numCourses))

        n = numCourses
        before_graph = defaultdict(list)
        after_graph = defaultdict(list)
        for a, b in prerequisites:
            before_graph[a].append(b)
            after_graph[b].append(a)

        ans = []
        key_data = before_graph.keys()
        for i in range(n):
            if i not in key_data:
                ans.append(i)

        res = []
        while ans:
            ref = ans.pop()
            if ref not in res:
                res.append(ref)
            ref_data = after_graph[ref]
            for i in ref_data:
                before_graph[i].remove(ref)
                if not before_graph[i]:
                    ans.append(i)
                    res.append(i)
        if len(res) == n:
            return res
        return []
