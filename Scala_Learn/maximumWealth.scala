object Solution {
    def maximumWealth(accounts: Array[Array[Int]]): Int = {
        var ans = 0
        for (i <- accounts){
            if (i.sum > ans){
                ans = i.sum
            }
        }
        ans

    }
}