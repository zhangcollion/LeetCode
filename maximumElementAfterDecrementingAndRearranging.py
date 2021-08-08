class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if not arr:
            return 0
        ans = [1]
        arr.sort()
        for i in range(1, len(arr)):
            tmp = ans[-1]
            if tmp == arr[i]:
                ans.append(tmp)
                continue
            if tmp + 1 == arr[i] :
                ans.append(tmp+ 1)
                continue
            if tmp - 1 == arr[i]:
                ans.append(tmp-1)
                continue
            if arr[i] > tmp + 1:
                ans.append(tmp+1)
        return max(ans)

