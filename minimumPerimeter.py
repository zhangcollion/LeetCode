class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n_num = 1
        while 2 * n_num * (n_num + 1) * (2 * n_num + 1) < neededApples:
            n_num += 1
        return n_num * 8
