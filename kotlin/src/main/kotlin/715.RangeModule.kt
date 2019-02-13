import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/range-module/submissions/


class RangeModule{
  var ranges = listOf<Int>()

  fun addRange(left: Int, right: Int) {
    val n = ranges.size
    var (i, j) = 0 to n-1
    while(i<n && ranges[i] < left)
      i++
    while(j>=0 && ranges[j] > right)
      j--
    val cur = ranges.slice(0 until i).toMutableList()
    if(i % 2 == 0)
      cur.add(left)
    if((j+1) % 2 == 0)
      cur.add(right)
    ranges = cur + ranges.slice(j+1 until n)
  }

  fun queryRange(left: Int, right: Int): Boolean {
    val n = ranges.size
    var (l, r) = 0 to n-1
    while(l <= r){
      val m = (l+r)/2
      if(ranges[m] <= left)
        l = m+1
      else
        r = m-1
    }
    return r>=0 && (r%2 == 0) && ranges[r+1] >= right
  }

  fun removeRange(left: Int, right: Int) {
    val n = ranges.size
    var (i, j) = 0 to n-1
    while(i<n && ranges[i] <= left)
      i++
    while(j>=0 && ranges[j] >= right)
      j--
    val cur = ranges.slice(0 until i).toMutableList()
    if(i % 2 == 1)
      cur.add(left)
    if((j+1) % 2 == 1)
      cur.add(right)
    ranges = cur + ranges.slice(j+1 until n)
  }

  @Test
  fun test1(){
    addRange(10, 20)
    removeRange(14, 16)
    assertEquals(true, queryRange(10, 14))
    assertEquals(false, queryRange(13, 15))
    assertEquals(true, queryRange(16, 17))
  }
}