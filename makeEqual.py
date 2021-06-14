from typing import List
from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        dict_info = collections.defaultdict(lambda x :0)
        for word in words:
            for ele in word:
                if ele not in  dict_info:
                    dict_info[ele] = 1
                else:
                    dict_info[ele] = dict_info[ele] +1
        for i in dict_info.keys():
            if dict_info[i] % n != 0:
                return False
        
        return True