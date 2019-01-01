import org.junit.Assert.assertEquals
import org.junit.Test
import kotlin.arrayOf as arr
import kotlin.intArrayOf as iarr
//https://leetcode.com/problems/spiral-matrix/

class SpiralMatrix{
  fun spiralOrder(matrix: Array<IntArray>): List<Int> {
    val result = mutableListOf<Int>()
    if(matrix.isEmpty()) return result

    var turn=0
    val steps = mutableListOf(matrix[0].size, matrix.size)

    var i=0
    var j=-1
    var di=0
    var dj=1

    while(steps[turn] > 0){
      (1..steps[turn]).forEach{
        i += di
        j += dj
        result.add(matrix[i][j])
      }
      turn = turn xor 1
      steps[turn] --
      val tmp=di
      di = dj
      dj = -tmp
    }

    return result
  }

  @Test
  fun test1(){
    assertEquals(listOf(1,2,3,6,9,8,7,4,5), spiralOrder(arr(
        iarr(1, 2, 3),
        iarr(4, 5, 6),
        iarr(7, 8, 9)
    )))
  }

  @Test
  fun test2(){
    assertEquals(listOf(1,2,3,4,8,12,11,10,9,5,6,7), spiralOrder(arr(
        iarr(1, 2, 3, 4),
        iarr(5, 6, 7, 8),
        iarr(9,10,11,12)
    )))
  }
}
