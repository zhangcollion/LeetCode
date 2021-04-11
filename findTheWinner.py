class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return n
        if k == 1:
            return n
        data = list(range(1, n+1))
        start_point = 0
        while len(data)!=1:
            remove_point = start_point+k-1
            remove_point = remove_point%len(data)
            data.pop(remove_point)
            start_point = remove_point

        return data[0]



if __name__ == "__main__":
    n = 6
    k = 5
    print(Solution().findTheWinner(n, k))