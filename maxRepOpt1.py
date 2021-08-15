class Solution:
    def maxRepOpt1(self, text: str) -> int:
    
        def get_ans(data, originl):
            info = Counter(data)
            i = 0
            max_ans = -1
            ref = ""
            ans = 0
            flag = 0
            j = 0
            while i < len(data):
                if not ref or data[i] == ref and info[ref] > 0:
                    ref = data[i]
                    i += 1
                    ans += 1
                    info[ref] -= 1
                    continue
                else:
                    if info[ref] > 0 and flag == 0:
                        ans += 1
                        j = i
                        i += 1
                        info[ref] -= 1
                        flag = 1
                    else:
                        max_ans = max(max_ans, ans)
                        ref = ""
                        ans = 0
                        if flag == 1:
                            i = j
                        info = originl
                        flag = 0
            max_ans = max(max_ans, ans)
            return max_ans
        
        ans= -1
        for i in [text, text[::-1]]:
            tmp = get_ans(i, Counter(i))
            ans = max(tmp, ans)

        return ans