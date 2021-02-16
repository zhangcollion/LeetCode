class Solution:
    """
    def letterCasePermutation(self, S: str) -> List[str]:
        tmp_list = []
        for i in range(0, len(S)):
            if S[i].isalpha():
                tmp_save = []
                if len(tmp_list) == 0:
                    tmp_save.append( S[i].upper())
                    tmp_save.append( S[i].lower())
                else:
                    for j in range(0, len(tmp_list)):
                        tmp_save.append(tmp_list[j] + S[i].upper())
                        tmp_save.append(tmp_list[j] + S[i].lower())
                tmp_list = tmp_save
            else:
                if len(tmp_list) == 0:
                    tmp_list.append( S[i])
                else:
                    for j in range(0, len(tmp_list)):
                        tmp_list[j] += S[i]
        return (tmp_list)

    """

    def letterCasePermutation(self, S: str) -> List[str]:
        tmp_list = [[]]
        for i in range(0, len(S)):
            n = len(tmp_list)
            if S[i].isalpha():
                for i in range(0, n):
                    tmp_list.append(tmp_list[i][:])
                    tmp_list[i].append( S[i].upper())
                    tmp_list[i+1].append( S[i].lower())
            else:
                for j in range(0, len(tmp_list)):
                    tmp_list[j].append(S[i])


        return (tmp_list)