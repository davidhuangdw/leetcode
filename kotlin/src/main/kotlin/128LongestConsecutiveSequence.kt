import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/longest-consecutive-sequence/

class LongestConsecutiveSequence{
  fun longestConsecutive(nums: IntArray): Int {
    val remain = nums.toHashSet()
    var result = 0
    while(remain.isNotEmpty()){
      val v = remain.first()
      remain.remove(v)
      var count = 1
      for(dir in listOf(-1, 1)){
        var next = v+dir
        while(remain.contains(next)){
          count ++
          remain.remove(next)
          next += dir
        }
      }
      result = maxOf(result, count)
    }

    return result
  }

  @Test
  fun test1(){
    assertEquals(4, longestConsecutive(intArrayOf(100, 4, 200, 1, 3, 2)))
  }
}