
object Solution {
    def finalValueAfterOperations(operations: Array[String]): Int = {
        var ans = 0
        for (opt <- operations){
            if (opt.contains("+")==true){
                ans += 1
            }else{
                ans -= 1
            }
        }
        ans

    }
}