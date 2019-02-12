import org.junit.Assert.assertEquals
import org.junit.Test
import java.lang.Math.abs

//https://leetcode.com/problems/24-game/


class Game24{
  fun judgePoint24(nums: IntArray): Boolean {
    return cal(nums.map{ it.toDouble() })
  }

  private fun cal(nums: List<Double>): Boolean{
    val n = nums.size
    if(n == 1)
      return abs(nums[0] - 24) < 1e-6

    for(i in 0 until n)
      for(j in 0 until n) {
        if (i == j) continue
        val rem = nums.filterIndexed{k,_ -> k!=i && k!=j}
        val s = mutableSetOf(nums[i]+nums[j], nums[i]-nums[j], nums[i]*nums[j])
        if(nums[j] != 0.0)
          s.add(nums[i] / nums[j])
        for(x in s)
          if(cal(rem + listOf(x)))
            return true
      }

    return false
  }

  @Test
  fun test1(){
    assertEquals(true, judgePoint24(intArrayOf(4,1,8,7)))
  }

  @Test
  fun test2(){
    assertEquals(false, judgePoint24(intArrayOf(1,2,1,2)))
  }

  @Test
  fun test3(){
    assertEquals(true, judgePoint24(intArrayOf(3,3,8,8)))
  }

}