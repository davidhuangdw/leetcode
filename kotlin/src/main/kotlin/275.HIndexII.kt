import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/h-index-ii/


class HIndexII{
  fun hIndex(citations: IntArray): Int {
    val n = citations.size
    var (l, r) = 0 to n-1
    while(l <= r){
      val m = (r-l)/2 + l
      if(citations[m] >= n-m)
        r = m-1
      else
        l = m+1
    }
    return n-l
  }

  @Test
  fun test1(){
    assertEquals(3, hIndex(intArrayOf(0,1,3,5,6)))
  }

  @Test
  fun test2(){
    assertEquals(0, hIndex(intArrayOf()))
  }
}