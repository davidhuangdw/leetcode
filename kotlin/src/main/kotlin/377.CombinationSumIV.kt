import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/combination-sum-iv/


class CombinationSumIV{
  fun combinationSum4(nums: IntArray, target: Int): Int {
    val dp = IntArray(target+1)
    dp[0] = 1
    for(t in 1..target)
      for(v in nums)
        if(t-v >= 0)
          dp[t] += dp[t-v]
    return dp[target]
  }

  @Test
  fun test1(){
    assertEquals(7, combinationSum4(intArrayOf(1,2,3), 4))
  }
}