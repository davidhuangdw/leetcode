import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/largest-divisible-subset/


class LargestDivisibleSubset{
  fun largestDivisibleSubset(nums: IntArray): List<Int> {
    nums.sort()
    val dp = mutableListOf<List<Int>>()
    val n = nums.size
    for(i in 0 until n)
      dp.add((0 until i).filter{ nums[i]%nums[it] == 0 }.map{dp[it]+nums[i]}.maxBy{ it.size } ?: listOf(nums[i]))
    return dp.maxBy{ it.size } ?: emptyList()
  }

  @Test
  fun test1(){
    assertEquals(listOf(1,2), largestDivisibleSubset(intArrayOf(1,2,3)))
  }

  @Test
  fun test2(){
    assertEquals(listOf(1,2,4,8), largestDivisibleSubset(intArrayOf(1,2,4,8)))
  }
}