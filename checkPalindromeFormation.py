class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) == 1 or not a:
            return True
        b_rev = "".join(i for i in list(b)[::-1])
        if a == b_rev:
            return True
        if a[-1] == b_rev[-1]:
            return True
        return False

