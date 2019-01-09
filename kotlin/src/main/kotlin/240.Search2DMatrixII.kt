import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/search-a-2d-matrix-ii/


class Search2DMatrixII{
  fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
    if(matrix.isEmpty()) return false

    val n = matrix.size
    var i = 0
    var j = matrix[0].size-1
    while(i<n && j>=0){
      if(matrix[i][j] == target)
        return true
      else if(matrix[i][j] < target)
        i++
      else
        j--
    }
    return false
  }

  @Test
  fun tes1(){
    val matrix = arrayOf(
        intArrayOf(1,   4,  7, 11, 15),
        intArrayOf(2,   5,  8, 12, 19),
        intArrayOf(3,   6,  9, 16, 22),
        intArrayOf(10, 13, 14, 17, 24),
        intArrayOf(18, 21, 23, 26, 30)
    )
    assertEquals(true, searchMatrix(matrix, 5))
  }
}