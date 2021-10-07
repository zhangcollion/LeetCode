object Solution {
    def subtractProductAndSum(n: Int): Int = {
       val arr = n.toString.toCharArray.map(_.toString.toInt)
       arr.product - arr.sum
    }
}


object Solution {
    def subtractProductAndSum(n: Int): Int = {
        var ans = 0
        var mu_ans = 1
        var m = n
        var tmp = 0
        while (m >= 10){
            tmp = m % 10
            m = m/10
            ans += tmp
            mu_ans = mu_ans * tmp
        }
        ans += m
        mu_ans = mu_ans * m
        mu_ans - ans
    }
}