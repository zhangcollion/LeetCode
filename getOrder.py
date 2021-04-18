from typing import List
from collections import deque, defaultdict

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        data = [i for i, j in tasks]
        start_time = min(data)
        ans = []
        while len(ans) != len(tasks):
            min_time = 1000000000000
            for idx, ele in enumerate(tasks):
                start, keep = ele
                if idx not in ans:
                    if start <= start_time:
                        if min_time > keep:
                            use_data = idx
                            keep_time = keep
                            new_time = start
                            min_time = keep
            # jobs 中持续时间最短的

            ans.append(use_data)
            start_time = new_time + keep_time

        return ans

if __name__=="__main__":
    tasks =   [[7,10],[7,12],[7,5],[7,4],[7,2]]
    print(Solution().getOrder(tasks))