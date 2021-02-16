class Solution:
    def convertToBase7(self, num: int) -> str:
        end = num
        num = abs(num)
        result = ''
        if num < 7:
            result += str(num )
            if end < 0:
                result = "-" + result
        else:
            while num >= 7:
                result += str(num % 7)
                num = int(num / 7)
            result += str(num)
            if end < 0:
                result = "-" + result[::-1]
            else:
                result = result[::-1]
        return (result)



if __name__ == "__main__":
    W = -7
    print(Solution().convertToBase7(W))