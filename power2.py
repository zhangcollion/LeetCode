from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        data_list = []
        re = []
        # while N >10:
        #     re.append(N%10)
        #     N = int(N/10)
        # re.append(N)
        for item in permutations(str(N)):
            print(type(item))
            data = ""
            if int(item[0]) != 0:
                for i in list(item):
                    data += "".join(i)
                data = int(data)
                print(data)
                if (data & data - 1) == 0:
                    return True

        return False


if __name__ == "__main__":
    W = 46
    print(Solution().reorderedPowerOf2(W))
