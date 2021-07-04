
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        str_n  = str(n)
        if str_n[-1] in ["0","2","4","6","8"]:
            odd_num = n//2 
            ji_num = n//2
            ans = pow(5, odd_num, 1000000007) * pow(4, ji_num, 1000000007) % 1000000007     
            return ans
        else:
            odd_num = n //2+1 
            ji_num = n//2
            ans = pow(5, odd_num, 1000000007) * pow(4, ji_num, 1000000007) % 1000000007      
            return ans 