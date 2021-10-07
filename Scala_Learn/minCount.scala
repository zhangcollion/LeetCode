object Solution {
    def minCount(coins: Array[Int]): Int = {
        var  ans = 0
        for (coin <- coins){
            if (coin%2 == 0){
                ans += coin/2
            }else{
                ans += coin/2
                ans += 1
            }
            
        }
        ans

    }
}