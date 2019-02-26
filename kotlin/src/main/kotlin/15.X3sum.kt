import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/3sum


class X3sum {
  fun threeSum(nums: IntArray): List<List<Int>> {
    val n = nums.size
    nums.sort()     // to help uniqueness
    val lastIndex = hashMapOf<Int, Int>()
    for((i, v) in nums.withIndex())
      lastIndex[v] = i

    val res = mutableListOf<List<Int>>()
    for(i in 0 until n) {
      if(i-1 >= 0 && nums[i] == nums[i-1])
        continue
      for (j in i + 1 until n) {
        if(j-1 > i && nums[j] == nums[j-1])
          continue
        val s = nums[i] + nums[j]
        if(j < lastIndex.getOrDefault(-s, 0))
          res.add(listOf(nums[i], nums[j], -s))
      }
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(listOf(listOf(-1, -1, 2), listOf(-1, 0, 1)), threeSum(intArrayOf(-1, 0, 1, 2, -1, -4)))
  }

  @Test
  fun test2(){
    assertEquals(listOf(listOf(0, 0, 0)), threeSum(intArrayOf(0, 0, 0, 0)))
  }

}

