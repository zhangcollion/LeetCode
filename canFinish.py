from typing import List
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = True

        for i, j in prerequisites:
            edges[j].append(i)

        def dfs(ele):
            nonlocal valid
            visited[ele] = 1
            for i in edges[ele]:
                if visited[i] == 0:
                    dfs(i)
                    if not valid:
                        return
                if visited[i] == 1:
                    valid = False
                    return
            visited[ele] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


        return valid
if __name__=="__main__":
    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    s = Solution()
    print(s.canFinish(numCourses, prerequisites))