class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        def nextPermutation(nums: List[str]):
            if not nums:
                return 
            for i in range(len(nums)-1,0,-1):
                if nums[i] > nums[i-1]:
                    ref = nums[i-1]
                    min_max_data = nums[i]
                    index = i
                    for j in range(i+1, len(nums)):
                        if nums[j] > ref and min_max_data > nums[j]:
                            index = j
                            min_max_data = nums[j]
                    nums[index], nums[i-1] = ref, min_max_data
                    data = nums[i:]
                    data.sort()
                    nums[i:]=data
                    return
            nums.reverse()
        
        num = list(num)
        nums_min = num[:]

        for i in range(k):
            nextPermutation(nums_min)



        ans = 0
        for i in range(len(num)):
            if num[i] != nums_min[i]:
                for j in range(i+1, len(num)):
                    if num[j] == nums_min[i]:
                        for k in range(j-1, i-1, -1):
                            ans += 1
                            num[k], num[k+1] = num[k+1], num[k]
                        break
        return ans