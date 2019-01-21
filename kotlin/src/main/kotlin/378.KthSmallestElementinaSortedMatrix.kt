import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


class KthSmallestElementinaSortedMatrix{
  fun kthSmallest(matrix: Array<IntArray>, k: Int): Int {
    val (n, m) = matrix.size to matrix[0].size
    val que = PriorityQueue<Pair<Int, Int>>(compareBy{ matrix[it.first][it.second] })
    que.add(0 to 0)
    for(x in k-1 downTo 1){
      val (i, j) = que.poll()
      if(j+1 < m) que.add(i to j+1)
      if(j == 0 && i+1 < n) que.add(i+1 to j)
    }
    val (i, j) = que.peek()
    return matrix[i][j]
  }

  @Test
  fun test1(){
    assertEquals(14, kthSmallest(arrayOf(
        intArrayOf(1,5,9),
        intArrayOf(10,11,14),
        intArrayOf(12,13,15)
    ), 8))
  }
}
