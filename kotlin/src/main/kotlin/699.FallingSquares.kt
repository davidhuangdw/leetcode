import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/falling-squares/


class FallingSquares{
  class Node(val index: List<Int>, val begin: Int, val end: Int){
    val md = (begin + end)/2
    var reset: Int? = null
    var max = 0
    val left by lazy { Node(index, begin, md) }
    val right by lazy { Node(index, md, end) }

    fun pushdown(){
      if(reset == null) return
      left.reset = reset
      right.reset = reset
      reset = null
    }

    fun getmax() = reset ?: max

    fun query(l: Int, r: Int): Int{
      if(r <= index[begin] || index[end] <= l)
        return 0
      return reset ?: if(l <= index[begin] && index[end] <= r) max else maxOf(left.query(l, r), right.query(l, r))
    }

    fun update(l: Int, r: Int, v: Int){
      if(r <= index[begin] || index[end] <= l)
        return
      if(l <= index[begin] && index[end] <= r)
        reset = v
      else{
        pushdown()
        left.update(l, r, v)
        right.update(l, r, v)
        max = maxOf(left.getmax(), right.getmax())
      }
    }
  }

  fun fallingSquares(positions: Array<IntArray>): List<Int> {
    val s = mutableListOf<Int>()
    for((l, len) in positions)
      s.addAll(listOf(l, l+len))
    val index = s.sorted()
    val root = Node(index, 0, index.size-1)

    val res = mutableListOf<Int>()
    for((l, len) in positions){
      val r = l + len
      val h = root.query(l, r)
      root.update(l, r, h+len)
      res.add(root.getmax())
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(listOf(2, 5, 5), fallingSquares(arrayOf(
        intArrayOf(1, 2),
        intArrayOf(2, 3),
        intArrayOf(6, 1)
    )))
  }

  @Test
  fun test2(){
    assertEquals(listOf(100, 100), fallingSquares(arrayOf(
        intArrayOf(100, 100),
        intArrayOf(200, 100)
    )))
  }
}