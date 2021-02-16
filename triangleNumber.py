from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        self.res = 0
        if len(nums) < 3:
            return  0
        start  = 0
        self.data = []
        nums.sort()
        r = self.get_trigle_num(start,nums)
        return (self.res)

    def get_trigle_num(self,start, nums ):
        if len(self.data) == 3:
            if self.data[0] + self.data[1] > self.data[2]:
                self.res += 1
            else:
                return -1
            return
        for i in range(start, len(nums)):
            self.data.append(nums[i])
            flag = self.get_trigle_num(i+1, nums)
            self.data.pop()
            if -1 == flag:
                break


if __name__ == "__main__":
    W = [14,55,8,43,80,64,60,4,73,49,36,91,76,94,62,22,10,91,91,96,55,100,67,52,68,70,15,8,58,4,36,30,19,88,51,3,62,70,13,7,84,55,59,65,69,36,48,7,19,6,39,0,67,8,78,69,90,33,89,80,85,76,87,10,86,73,19,90,17,29,86,45,89,43,75,20,66,25,99,36,14,78,82,92,67,85,97,16,5,11,29,60,46,64,27,96,92,67,65,41]
    print(Solution().triangleNumber(W))