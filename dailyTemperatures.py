class Solution(object):
    def dailyTemperatures(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[T[i]+1: 102])
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans



if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))