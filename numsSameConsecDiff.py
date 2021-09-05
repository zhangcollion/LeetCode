class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        data = list(range(0, 10))
        ans = []

        def get_ans(tmp):
            if len(tmp) == n:
                if tmp[0]!= "0":
                    ans.append(int(tmp))
                return
                
            tmp_data = list(set([int(tmp[-1])-k, int(tmp[-1])+k]))
            for ele in tmp_data:
                if 0<=ele<=9:
                    get_ans(tmp+str(ele))

        for i in range(1, 10):
            get_ans(str(i))
        return ans
            
