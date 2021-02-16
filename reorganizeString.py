import collections

class Solution:
    def reorganizeString(self, S: str) -> str:
        word_dict = dict(collections.Counter(S))
        re = ""
        while word_dict:
            word_dict = dict(sorted(word_dict.items(), key=lambda item:-item[1]))
            key = list(word_dict.keys())
            ele = key[0]
            if re == "":
                re += ele
                word_dict[ele] -= 1
                if word_dict[ele] == 0:
                    del word_dict[ele]
            else:
                if re[-1] == ele:
                    if len(key) == 1:
                        return ""
                    else:
                        i = 1
                        while i < len(key):
                            ele = key[i]
                            if re[-1] != ele:
                                re += ele
                                word_dict[ele] -= 1
                                if word_dict[ele] == 0:
                                    del word_dict[ele]
                                break
                            else:
                                i += 1
                else:
                    re += ele
                    word_dict[ele] -= 1
                    if word_dict[ele] == 0:
                        del word_dict[ele]
        print(re)
        return re



if __name__ == "__main__":
    W = "baaba"
    print(Solution().reorganizeString(W))