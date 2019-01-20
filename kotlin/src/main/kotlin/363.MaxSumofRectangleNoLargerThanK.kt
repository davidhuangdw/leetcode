import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
import java.util.*


class MaxSumofRectangleNoLargerThanK{
  fun maxSumSubmatrix(matrix: Array<IntArray>, k: Int): Int {
    var reverse = false
    var n = matrix.size
    var m = matrix[0].size
    if(n > m){
      reverse = true
      val t = n; n = m; m = t
    }

    var ret = Int.MIN_VALUE
    for(fr in 0 until n) {
      val cols = IntArray(m)
      for (to in fr until n) {
        var sum = 0
        val set = TreeSet<Int>()
        set.add(0)
        for(j in 0 until m) {
          cols[j] += if(reverse) matrix[j][to] else matrix[to][j]
          sum += cols[j]
          val min = set.ceiling(sum - k)
          if(min != null) ret = maxOf(ret, sum-min)
          set.add(sum)
        }
      }
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(2, maxSumSubmatrix(arrayOf(
        intArrayOf(1,0,1),
        intArrayOf(0,-2,3)
    ),2))
  }
}