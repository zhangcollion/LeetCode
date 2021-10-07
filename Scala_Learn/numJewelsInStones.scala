object Solution {
    def numJewelsInStones(jewels: String, stones: String): Int = {
        var ans = 0
        for (str <- stones){
            if (jewels.contains(str)==true){
                ans += 1
            }
        }
        ans
    }
}