import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*
import kotlin.collections.HashMap

//https://leetcode.com/problems/the-skyline-problem/


class TheSkylineProblem{
  class MultiSet<T>{
    private val count = HashMap<T, Int>()
    val que = PriorityQueue<T>(Collections.reverseOrder())
    fun add(v: T){
      que.add(v)
      count[v] = count.getOrDefault(v, 0) + 1
    }
    fun remove(v: T){
      count[v] = count[v]!! - 1
    }
    fun empty(): Boolean{
      cleanup()
      return que.isEmpty()
    }
    fun max(): T{
      cleanup()
      return que.peek()
    }
    private fun cleanup(){
      while(que.isNotEmpty() && count[que.peek()]!! == 0)
        que.poll()
    }
  }

  data class End(val x: Int, val y:Int, val up: Boolean)

  fun getSkyline(buildings: Array<IntArray>): List<IntArray> {
    if(buildings.isEmpty()) return emptyList()

    val points = mutableListOf<End>()
    for(b in buildings){
      val (l, r, h) = b
      points.add(End(l, h, true))
      points.add(End(r, h, false))
    }
    points.sortWith(compareBy({it.x}, {!it.up}))

    val set = MultiSet<Int>()
    val result = mutableListOf<IntArray>(intArrayOf(points[0].x, points[0].y))
    set.add(points[0].y)
    for(p in points.subList(1, points.size))
      if(p.up){
        set.add(p.y)
        val last = result.last()
        if(last[1] < p.y){
          if(last[0] == p.x)
            last[1] = p.y
          else
            result.add(intArrayOf(p.x, p.y))
        }
      } else{
        set.remove(p.y)
        if (set.empty() || p.y > set.max()){
          val cur = if(set.empty()) 0 else set.max()
          if(result.last()[0] == p.x)
            result.last()[1] = cur
          else
            result.add(intArrayOf(p.x, cur))
        }
      }
    return result
  }

  @Test
  fun test1(){
    val expected = listOf(
        intArrayOf(2, 10),
        intArrayOf(3, 15),
        intArrayOf(7, 12),
        intArrayOf(12, 0),
        intArrayOf(15, 10),
        intArrayOf(20, 8),
        intArrayOf(24, 0)
    )
    val buildings = arrayOf(
        intArrayOf(2, 9, 10),
        intArrayOf(3, 7, 15),
        intArrayOf(5, 12, 12),
        intArrayOf(15, 20, 10),
        intArrayOf(19, 24, 8)
    )
    assertEquals(expected.map{it.toList()}, getSkyline(buildings).map{it.toList()})
  }

  @Test
  fun test2(){
    val expected = listOf(
        intArrayOf(0, 3),
        intArrayOf(5, 0)
    )
    val buildings = arrayOf(
        intArrayOf(0, 2, 3),
        intArrayOf(2, 5, 3)
    )
    assertEquals(expected.map{it.toList()}, getSkyline(buildings).map{it.toList()})
  }

  @Test
  fun test3(){
    val expected = listOf(
        intArrayOf(2, 7),
        intArrayOf(4, 0)
    )
    val buildings = arrayOf(
        intArrayOf(2, 4, 7),
        intArrayOf(2, 4, 5),
        intArrayOf(2, 4, 6)
    )
    assertEquals(expected.map{it.toList()}, getSkyline(buildings).map{it.toList()})
  }
}
