object Solution {
    def numberOfSteps(num: Int): Int = {
       var ans = 0
       var n = num
       while(n>0){
           if(n%2==0){
               ans += 1
               n = n/2
           }else{
               ans += 1
               n = n-1
           }
       }
    
    ans

    }
}