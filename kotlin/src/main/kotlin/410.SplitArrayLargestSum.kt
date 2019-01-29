import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/split-array-largest-sum/


class SplitArrayLargestSum{
  fun splitArray(nums: IntArray, m: Int): Int {
    val n = nums.size
    val sums = IntArray(n+1)
    val dp = IntArray(n+1)
    for(i in 0 until n) {
      sums[i + 1] = sums[i] + nums[i]
      dp[i+1] = sums[i+1]
    }

    for(r in 2..m){
      var k = n-1
      for(i in n downTo r){
        fun cal(j: Int) = maxOf(dp[j], sums[i]-sums[j])
        while(k >= r && cal(k-1) <= cal(k))
          k--
        dp[i] = cal(k)
      }
    }

    return dp[n]
  }

  @Test
  fun test1(){
    assertEquals(18, splitArray(intArrayOf(7,2,5,10,8), 2))
  }
}