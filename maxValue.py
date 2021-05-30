class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == "-":
            new_data = []
            flag = 0
            new_data.append(n[0])
            for i in range(1, len(n)):
                if int(x) < int(n[i]):
                    new_data.append(str(x))
                    flag = 1
                    break
                else:
                    new_data.append(n[i])

            if flag == 1:

                new_data.append(n[i:])
            else:
                new_data.append(str(x))

            return "".join(new_data)

        else:
            flag = 0
            new_data = []
            for i in range(0, len(n)):
                if int(x) > int(n[i]):
                    new_data.append(str(x))
                    flag = 1
                    break
                else:
                    new_data.append(n[i])
            if flag == 1:

                new_data.append(n[i:])
            else:
                new_data.append(str(x))

            return "".join(new_data)

