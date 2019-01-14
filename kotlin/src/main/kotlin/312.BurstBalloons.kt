import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/burst-balloons/


class BurstBalloons{
  fun maxCoins(nums: IntArray): Int {
    val values = listOf(1) + nums.filter{it > 0}  + listOf(1)
    val n = values.size

    val dp = Array<IntArray>(n){ IntArray(n) }
    for(w in 2 until n)
      for(l in 0 until n-w){
        val r = l+w
        for(k in l+1 until r)
          dp[l][r] = maxOf(dp[l][r], dp[l][k] + dp[k][r] + values[l]*values[k]*values[r])
      }
    return dp[0][n-1]
  }

  @Test
  fun test1(){
    assertEquals(167, maxCoins(intArrayOf(3,1,5,8)))
  }

  @Test
  fun test2(){
    assertEquals(0, maxCoins(intArrayOf(0,0)))
  }
}