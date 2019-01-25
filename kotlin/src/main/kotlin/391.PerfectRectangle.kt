import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/perfect-rectangle/


class PerfectRectangle{
  fun isRectangleCover(rectangles: Array<IntArray>): Boolean {
    var (glx, gly, grx, gry) = intArrayOf(Int.MAX_VALUE, Int.MAX_VALUE, 0, 0)
    var sum = 0
    val points = HashSet<Pair<Int, Int>>()

    fun merge(rect: IntArray){
      val (lx, ly, rx, ry) = rect
      for(point in listOf(lx to ly, lx to ry, rx to ly, rx to ry)){
        if(points.contains(point))
          points.remove(point)
        else
          points.add(point)
      }
    }
    for(r in rectangles){
      val (lx, ly, rx, ry) = r
      sum += (rx-lx)*(ry-ly)
      merge(r)
      glx = minOf(glx, lx)
      gly = minOf(gly, ly)
      grx = maxOf(grx, rx)
      gry = maxOf(gry, ry)
    }
    merge(intArrayOf(glx, gly, grx, gry))
    return points.isEmpty() && sum == (gry-gly)*(grx-glx)
  }

  @Test
  fun test1(){
    assertEquals(true, isRectangleCover(arrayOf(
        intArrayOf(1,1,3,3),
        intArrayOf(3,1,4,2),
        intArrayOf(3,2,4,4),
        intArrayOf(1,3,2,4),
        intArrayOf(2,3,3,4)
    )))
  }

  @Test
  fun test2(){
    assertEquals(false, isRectangleCover(arrayOf(
        intArrayOf(1,1,2,3),
        intArrayOf(3,1,4,2),
        intArrayOf(1,3,2,4),
        intArrayOf(3,2,4,4)
    )))
  }

  @Test
  fun test3(){
    assertEquals(false, isRectangleCover(arrayOf(
        intArrayOf(1,1,3,3),
        intArrayOf(3,1,4,2),
        intArrayOf(1,3,2,4),
        intArrayOf(2,2,4,4)
    )))
  }
}