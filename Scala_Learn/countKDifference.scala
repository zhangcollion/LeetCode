object Solution {
    def countKDifference(nums: Array[Int], k: Int): Int = {
        var ans = 0
        val n = nums.length
        for (i <- 0 until n){
            val a =  nums(i) + k 
            val b = nums(i) - k
            for (j <- i until n){
                if (nums(j) == a | nums(j) == b){
                    ans += 1
                }
            }
        }
        ans
    }
}