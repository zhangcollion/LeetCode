class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        info = {}
        char_data = []
        for i in range(97, 99 + 26):
            char_data.append(chr(i))
        for i, j in zip(char_data, range(0, 26)):
            info[i] = j
        a1 = 0
        for i in firstWord:
            if i == "a" and a1 == 0:
                continue
            else:
                a1 = a1 * 10 + info[i]
        a2 = 0
        for i in secondWord:
            if i == "a" and a2 == 0:
                continue
            else:
                a2 = a2 * 10 + info[i]
        a3 = 0
        for i in targetWord:
            if i == "a" and a3 == 0:
                continue
            else:
                a3 = a3 * 10 + info[i]

        return a1 + a2 == a3