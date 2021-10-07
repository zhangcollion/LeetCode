object Solution {
    def maxProductDifference(nums: Array[Int]): Int = {
        val a = nums.sorted
        val n = a.length
        a(n-1)*a(n-2)-a(1)*a(0)
    }
}