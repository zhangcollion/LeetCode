object Solution {
    def arraySign(nums: Array[Int]): Int = {
        
        var res = 1
        for(i <- nums){
            if (i==0){
                res = 0
            }
            if (i < 0){
                res *= -1
            }
        }
        res 
    }
}
