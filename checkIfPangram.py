from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        info = Counter(sentence)
        key = list(info.keys())
        # print(key)
        # print(len(key))
        if len(key) == 26:
            return True
        return False