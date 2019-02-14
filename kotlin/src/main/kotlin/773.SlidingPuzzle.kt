import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/sliding-puzzle/


class SlidingPuzzle{
  fun slidingPuzzle(board: Array<IntArray>): Int {
    var target = listOf<Int>()
    for(r in board)
      target = target + r.toList()

    val (R, C) = board.size to board[0].size
    val done = hashSetOf<List<Int>>()
    val que = LinkedList<Pair<Int, List<Int>>>()
    que.push(0 to (1 until R*C).toList() + listOf(0))
    while(que.isNotEmpty()){
      val (cnt, state) = que.pollLast()
      if(state == target) return cnt
      done.add(state)
      val i = state.indexOf(0)
      for(d in listOf(-1, 1, -C, C)){
        val j = i + d
        if((d == -1 && i%C == 0) || (d == 1 && j%C == 0)|| j !in (0 until R*C)) continue
        val list = state.toMutableList()
        val tmp = list[i]
        list[i] = list[j]
        list[j] = tmp
        val nextState = list.toList()
        if(nextState !in done)
          que.push(cnt+1 to nextState)
      }
    }
    return -1
  }

  @Test
  fun test1(){
    assertEquals(1, slidingPuzzle(arrayOf(intArrayOf(1,2,3), intArrayOf(4,0,5))))
  }

  @Test
  fun test2(){
    assertEquals(-1, slidingPuzzle(arrayOf(intArrayOf(1,2,3), intArrayOf(5,4,0))))
  }

  @Test
  fun test3(){
    assertEquals(5, slidingPuzzle(arrayOf(intArrayOf(4,1,2), intArrayOf(5,0,3))))
  }

}