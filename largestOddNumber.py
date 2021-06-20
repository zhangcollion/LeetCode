class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start_h, start_m = startTime.split(":")
        finish_h, finish_m = finishTime.split(":")    
        finish_h = int(finish_h)
        start_h = int(start_h)
        if (finish_h == start_h and int(finish_m) >= int(start_m)) :
                h = finish_h-start_h
                ans = h * 4
                if int(start_m) <= 0 and 15 <= int(finish_m):
                    ans += 1
                if int(start_m) <= 15 and 30 <= int(finish_m):
                    ans += 1
                if int(start_m) <= 30 and 45 <= int(finish_m):
                    ans += 1
                if int(start_m) <= 45 and 45 <= int(finish_m) and not finish_m.startswith("5"):
                    ans += 1
                return ans
        if finish_h > start_h:
            if int(start_m) == 0:
                h = finish_h-start_h 
                ans = h * 4
                if 0 <= int(finish_m) < 15:
                    ans += 0
                elif 15 <= int(finish_m) < 30 :
                    ans += 1
                elif 30 <= int(finish_m) < 45 :
                    ans += 2
                else:
                    ans += 3
                return ans
            else:
                h = finish_h-start_h - 1
                ans = h * 4
           
                if int(start_m) <= 15  :
                    ans += 3
                elif int(start_m) <= 30 :
                    ans += 2
                elif int(start_m) <= 45  :
                    ans += 1
                if 0 <= int(finish_m) < 15:
                    ans += 0
                elif 15 <= int(finish_m) < 30 :
                    ans += 1
                elif 30 <= int(finish_m) < 45 :
                    ans += 2
                else:
                    ans += 3
                return ans


        h = 23-start_h
        ans = h * 4
        if int(start_m) == 0 :
            ans += 4
        elif int(start_m) <= 15  :
            ans += 3
        elif int(start_m) <= 30 :
            ans += 2
        elif int(start_m) <= 45  :
            ans += 1
        h = finish_h 
        ans += h * 4
        if 0 <= int(finish_m) < 15:
            ans += 0
        elif 15 <= int(finish_m) < 30 :
            ans += 1
        elif 30 <= int(finish_m) < 45 :
            ans += 2
        else:
            ans += 3
        return ans
            
                
                
            
        