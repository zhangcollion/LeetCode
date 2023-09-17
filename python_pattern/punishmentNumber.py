class Solution:
    def punishmentNumber(self, n: int) -> int:

        def get_ans(df, ans, data):
            if sum(map(int, ans)) > data:
                return False
            if sum(map(int, ans)) == data and len(ans) > 1 and len(df) == 0:
                return True
            if len(df) == 0:
                return False
            for i in range(1, len(df) + 1):
                if int(df[0:i]) > data:
                    break
                if get_ans(df[i:], ans + [df[0:i]], data):
                    return True
            return False

        def is_valid(data):
            ref = data * data
            if ref == 1:
                return True
            else:
                res = []
                ans = []
                df = str(ref)
                for i in range(1, len(df) + 1):
                    if int(df[0:i]) > ref:
                        break
                    if get_ans(df[i:], ans + [df[0:i]], data):
                        return True
                return False
            return False

        result = []
        for i in range(1, n + 1):
            if is_valid(i):
                result.append(i * i)
        return sum(result)


if __name__ == "__main__":
    print(Solution().punishmentNumber(10))