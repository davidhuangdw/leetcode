import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/game-of-life


class GameofLife{
  fun gameOfLife(board: Array<IntArray>): Unit {
    if(board.isEmpty()) return

    val n = board.size
    val m = board[0].size
    for(i in 0 until n)
      for(j in 0 until m){
        var cnt = 0
        for(x in maxOf(i-1, 0)..minOf(i+1,n-1))
          for(y in maxOf(j-1, 0)..minOf(j+1,m-1))
            if((board[x][y] and 1) != 0)
              cnt ++
        if(cnt == 3 || cnt-board[i][j] == 3)
          board[i][j] = board[i][j] or 2
      }

    for(i in 0 until n)
      for(j in 0 until m)
        board[i][j] = board[i][j] ushr 1
  }

  @Test
  fun test1(){
    val board = arrayOf(
        intArrayOf(0,1,0),
        intArrayOf(0,0,1),
        intArrayOf(1,1,1),
        intArrayOf(0,0,0)
    )
    gameOfLife(board)
    assertEquals(listOf(
        listOf(0,0,0),
        listOf(1,0,1),
        listOf(0,1,1),
        listOf(0,1,0)
    ), board.toList().map{it.toList()})
  }
}