class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:   
        if arr[start] == 0:
            return True
        self.arr = arr
        self.seen = set()
        self.ans = False
        self.dfs(start)
        return self.ans
        
    def dfs(self,loc): 
        for i in (loc+self.arr[loc], loc-self.arr[loc]):
            if 0 <= i < len(self.arr):
                if i not in self.seen:
                    self.seen.add(i)
                    if self.arr[i] == 0:
                        self.ans = True
                        return 
                    else: 
                        self.dfs(i)
                if self.ans:
                    return


##  BFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:   
        if arr[start] == 0:
            return True


        seen = [start]
        check = set()
        while seen:
            loc = seen.pop()
            a, b = loc+arr[loc], loc-arr[loc]
            for j in [a, b]:
                if 0 <= j < len(arr) and j not in check:
                    if arr[j] == 0:
                        return True
                    check.add(j)
                    seen.append(j)
        return False