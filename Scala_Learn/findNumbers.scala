object Solution {
    def findNumbers(nums: Array[Int]): Int = {
        var ans = 0 
        for(i <- nums){
            var tmp = i.toString
            if(tmp.length%2 == 0){
                ans += 1
            }
        }
        ans
    }
}