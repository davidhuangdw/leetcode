import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/range-module


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

class RangeModuleBySegmentTree{
  class Node(val begin: Int, val end: Int, var reset: Boolean? = false){
    val md = (begin+end)/2
    val left by lazy { Node(begin, md) }
    val right by lazy { Node(md, end) }

    fun pushdown(){
      if(reset != null){
        left.reset = reset
        right.reset = reset
        reset = null
      }
    }

    fun update(l: Int, r: Int, state: Boolean){
      if(r <= begin || end <= l || reset==state) return
      if(l<=begin && end<=r)
        reset = state
      else {
        pushdown()
        left.update(l, r, state)
        right.update(l, r, state)
      }
    }

    fun covered(l: Int, r: Int): Boolean{
      return r <= begin || end <= l ||
          (reset ?: (left.covered(l, r) && right.covered(l, r)))
    }
  }

  val root = Node(0, 1e9.toInt())
  fun addRange(left: Int, right: Int) {
    root.update(left, right, true)
  }

  fun queryRange(left: Int, right: Int): Boolean {
    return root.covered(left, right)
  }

  fun removeRange(left: Int, right: Int) {
    root.update(left, right, false)
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