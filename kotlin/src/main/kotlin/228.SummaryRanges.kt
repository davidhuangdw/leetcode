import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/summary-ranges/


class SummaryRanges{
  private fun range(fr: Int, to: Int) = if(fr == to) "$fr" else "$fr->$to"

  fun summaryRanges(nums: IntArray): List<String> {
    val result = mutableListOf<String>()
    var l = 0
    for(i in 1..nums.size)
      if(i==nums.size || nums[i] != nums[i-1]+1){
        result.add(range(nums[l], nums[i-1]))
        l = i
      }
    return result
  }

  @Test
  fun test1(){
    assertEquals(listOf("0->2","4->5","7"), summaryRanges(intArrayOf(0,1,2,4,5,7)))
  }

  @Test
  fun test2(){
    assertEquals(listOf("0","2->4","6","8->9"), summaryRanges(intArrayOf(0,2,3,4,6,8,9)))
  }

  @Test
  fun test3(){
    assertEquals(listOf<String>(), summaryRanges(intArrayOf()))
  }
}