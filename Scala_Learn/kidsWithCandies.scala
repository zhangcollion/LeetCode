object Solution {
    def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
        
        var ans:List[Boolean] = List()
        val max_data = candies.max
        var j = 0
        for (i <- candies){
            if (i+extraCandies >= max_data){
                ans = true::ans
            }else{
                ans = false::ans
            }
        }
        ans.reverse
    }
}