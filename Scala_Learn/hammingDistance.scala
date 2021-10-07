object Solution {
    def hammingDistance(x: Int, y: Int): Int = {
        val a = (x ^ y).toBinaryString
        var ans = 0
        for(i<-a){
            if (i=='1'){
                ans += 1
            }
        }
        ans
    }
}