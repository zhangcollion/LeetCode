class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        tmp1 = True
        for i in range(0, len(s1)):
            if s1[i] < s2[i]:
                tmp1 = False
                break

        tmp2 = True
        for i in range(0, len(s1)):
            if s2[i] < s1[i]:
                tmp2 = False
                break

        return tmp1 or tmp2


                
