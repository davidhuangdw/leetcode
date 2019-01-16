import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class LongestIncreasingPathinaMatrix{
  fun longestIncreasingPath(matrix: Array<IntArray>): Int {
    val n = matrix.size
    if(n == 0) return 0
    val m = matrix[0].size
    val cache = Array(n){IntArray(m)}

    fun dp(i: Int, j: Int): Int{
      if(cache[i][j] > 0) return cache[i][j]
      cache[i][j] = 1
      for((ni, nj) in listOf(i to j+1, i to j-1, i+1 to j, i-1 to j))
        if(ni in 0 until n && nj in 0 until m && matrix[ni][nj] > matrix[i][j])
          cache[i][j] = maxOf(cache[i][j], dp(ni, nj)+1)
      return cache[i][j]
    }

    var mx= 0
    for(i in 0 until n)
      for(j in 0 until m)
        mx = maxOf(mx, dp(i, j))
    return mx
  }

  @Test
  fun test1(){
    assertEquals(4, longestIncreasingPath(arrayOf(
        intArrayOf(9,9,4),
        intArrayOf(6,6,8),
        intArrayOf(2,1,1)
    )))
  }

  @Test
  fun test2(){
    assertEquals(4, longestIncreasingPath(arrayOf(
        intArrayOf(3,4,5),
        intArrayOf(3,2,6),
        intArrayOf(2,2,1)
    )))
  }
}