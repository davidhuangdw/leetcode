import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/rectangle-area-ii/


class RectangleAreaII{
  data class Op(val x: Int, val y1: Int, val y2: Int, val add: Boolean)
  val MOD = 1e9.toLong() + 7
  fun rectangleArea(rectangles: Array<IntArray>): Int {
    val ops = mutableListOf<Op>()
    for((x1, y1, x2, y2) in rectangles){
      ops.add(Op(x1, y1, y2, true))
      ops.add(Op(x2, y1, y2, false))
    }
    ops.sortBy{ it.x }
    val intervals = TreeMap<Pair<Int, Int>, Int>(compareBy({it.first}, {it.second}))
    fun total(): Long{
      if(intervals.isEmpty()) return 0
      var sum = 0L
      var (l, r) = intervals.firstKey()
      for((a, b) in intervals.keys){
        if(a <= r)
          r = maxOf(r, b)
        else{
          sum += r-l
          l = a
          r = b
        }
      }
      return r - l + sum
    }
    var (pre, res) = 0 to 0L
    for((x, y1, y2, add) in ops){
      res = (res+(total()*(x-pre))) % MOD
      pre = x
      if(add)
        intervals[y1 to y2] = intervals.getOrDefault(y1 to y2, 0) + 1
      else {
        intervals[y1 to y2] = intervals[y1 to y2]!! - 1
        if(intervals[y1 to y2] == 0)
          intervals.remove(y1 to y2)
      }
    }
    return res.toInt()
  }

  @Test
  fun test0(){
    assertEquals(18, rectangleArea(arrayOf(
        intArrayOf(0,0,3,3),
        intArrayOf(2,0,5,3),
        intArrayOf(1,1,4,4)
    )))
  }

  @Test
  fun test1(){
    assertEquals(6, rectangleArea(arrayOf(
        intArrayOf(0,0,2,2),
        intArrayOf(1,0,2,3),
        intArrayOf(1,0,3,1)
    )))
  }

  @Test
  fun test2(){
    assertEquals(49, rectangleArea(arrayOf(
        intArrayOf(0,0,1000000000,1000000000)
    )))
  }
}