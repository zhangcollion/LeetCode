from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        if not graph:
            return self.ans

        end_point = len(graph)
        start_point = 0
        idx = 0
        self.get_ans(graph, [start_point], idx)

        return self.ans

    def get_ans(self, graph, ref, idx):

        if ref[-1] == len(graph) - 1:
            self.ans.append(ref)
            return
        if not graph[idx]:
            return
        data = graph[idx]
        for i in range(len(data)):
            self.get_ans(graph, ref+[data[i]], data[i])

if __name__ == "__main__":
    # candidates = [2, 3, 6, 7]
    heights = [[1,2,3],[2],[3],[]]
    print(Solution().allPathsSourceTarget(heights))
