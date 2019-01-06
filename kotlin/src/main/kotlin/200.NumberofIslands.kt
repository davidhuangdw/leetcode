import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*
import kotlin.collections.ArrayList

//https://leetcode.com/problems/number-of-islands/

class NumberofIsland{
  fun visit(grid: Array<CharArray>, i: Int, j: Int){
    val que = Stack<Pair<Int, Int>>()
    que.push(i to j)
    while(que.isNotEmpty()){
      val (i,j) = que.pop()
      grid[i][j] = 'x'
      for((di, dj) in listOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)){
        val ni = i + di
        val nj = j + dj
        if(0<=ni && ni<grid.size && 0<=nj && nj<grid[i].size && grid[ni][nj] == '1')
          que.push(ni to nj)
      }
    }
  }

  fun numIslands(grid: Array<CharArray>): Int {
    var count = 0
    for(i in 0 until grid.size)
      for(j in 0 until grid[i].size)
        if(grid[i][j] == '1'){
          count ++
          visit(grid, i, j)
        }
    return count
  }

  @Test
  fun test1(){
    assertEquals(1, numIslands(arrayOf(
        "11110",
        "11010",
        "11000",
        "00000"
    ).map{it.toCharArray()}.toTypedArray()))
  }

  @Test
  fun test2(){
    assertEquals(3, numIslands(arrayOf(
        "11000",
        "11000",
        "00100",
        "00011"
    ).map{it.toCharArray()}.toTypedArray()))
  }
}