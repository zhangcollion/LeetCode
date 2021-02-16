from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda e :(e[0], e[1]))
        result = []
        start,end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            data = intervals[i]
            left, right = data[0], data[1]
            if left <= end:
                end = max(end, right)
            else:
                result.append([start, end])
                start = left
                end = right
        result.append([start, end])
        return(result)








if __name__=="__main__":
    data = [[1,4],[4,5]]
    print(Solution().merge(data))