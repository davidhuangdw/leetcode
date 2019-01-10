import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/perfect-squares/


class PerfectSquares{
  fun numSquares(n: Int): Int {
    val cnt = IntArray(n+1){ n }
    val squares = mutableListOf(1)
    for(x in 2..n) {
      val s = x*x
      if (s > n) break
      squares.add(s)
      cnt[s] = 1
    }

    for(x in 2..n)
      for(s in squares)
        if(x+s > n || s > x)
          break
        else
          cnt[x+s] = minOf(cnt[x+s], cnt[x]+1)

    return cnt[n]
  }

  //bfs
  fun numSquares1(n: Int): Int {
    val squares = mutableListOf(1)
    for(x in 2..n) {
      val s = x * x
      if (s > n) break
      squares.add(s)
    }
    val set = mutableSetOf(0)
    var layer = mutableSetOf(0)
    var cnt = 0
    while(cnt <= n){
      cnt ++
      val next = mutableSetOf<Int>()
      for(v in layer)
        for(s in squares) {
          val x = v+s
          if (x == n) return cnt
          else if (x < n && !set.contains(x)) {
            set.add(x)
            next.add(x)
          }
        }
      layer = next
    }
    return -1
  }

  @Test
  fun test1(){
    assertEquals(3, numSquares(12))
  }

  @Test
  fun test2(){
    assertEquals(2, numSquares(13))
  }
}