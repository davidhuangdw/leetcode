import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/guess-number-higher-or-lower-ii/


class GuessNumberHigherorLowerII{
  // O(n^2): https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84826/An-O(n2)-DP-Solution-Quite-Hard.
  fun getMoneyAmount(n: Int): Int {
    val dp = Array(n+2){ IntArray(n+2) }
    for(r in 2..n) {
      var k = r
      val que = LinkedList<Pair<Int, Int>>()  // x to dp[x+1][r]+x
      for(l in r-1 downTo 1){
        val cur = dp[l+1][r] + l
        while(que.isNotEmpty() && que.peek().second >= cur)
          que.pop()
        que.push(l to cur)

        while(k-1 >=l && dp[l][k-1] > dp[k+1][r])
          k --
        while(que.last().first > k)
          que.pollLast()
        dp[l][r] = minOf(que.last().second, dp[l][k]+k+1)
      }
    }
    return dp[1][n]
  }

  @Test
  fun test1(){
    assertEquals(1, getMoneyAmount(2))
  }

  @Test
  fun test2(){
    assertEquals(10, getMoneyAmount(7))
  }
}