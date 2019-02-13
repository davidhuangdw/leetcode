import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/my-calendar-iii/


class MyCalendarIII{
  data class TreeNode(val begin: Int, val end: Int, var count: Int=0, var max: Int=0){
    var left: TreeNode? = null
    var right: TreeNode? = null
    val md = (begin+end)/2
    fun add(l: Int, r: Int){
      if(end < l || r < begin) return
      if(l<=begin && end<=r){
        count += 1
        max += 1
        return
      }
      if(left == null)
        left = TreeNode(begin, md)
      if(right == null)
        right = TreeNode(md+1, end)
      left!!.add(l, r)
      right!!.add(l, r)
      max = count + maxOf(left!!.max, right!!.max)
    }
  }

  val root = TreeNode(1, 1e9.toInt())

  fun book(start: Int, end: Int): Int {
    root.add(start, end-1)
    return root.max
  }

  @Test
  fun test1(){
    assertEquals(1, book(10, 20))
    assertEquals(1, book(50, 60))
    assertEquals(2, book(10, 40))
    assertEquals(3, book(5, 15))
    assertEquals(3, book(5, 10))
    assertEquals(3, book(25, 55))
  }

}