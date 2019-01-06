import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/find-peak-element/

class FindPeakElement{
  fun findPeakElement(nums: IntArray): Int {
    val n = nums.size
    var l = 0
    var r = n-1
    while(l <= r){
      val m = (r-l)/2+l
      if(m+1 < n && nums[m] < nums[m+1])
        l = m+1
      else if(m-1 >=0 && nums[m] < nums[m-1])
        r = m-1
      else
        return m
    }
    return -1
  }

  @Test
  fun test1(){
    assertEquals(2, findPeakElement(intArrayOf(1,2,3,1)))
  }

  @Test
  fun test2(){
    assert(findPeakElement(intArrayOf(1,2,1,3,5,6,4)) in listOf(1, 5))
  }
}