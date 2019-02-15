import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/bus-routes/


class BusRoutes{
  fun numBusesToDestination(routes: Array<IntArray>, S: Int, T: Int): Int {
    if(S == T) return 0
    val n = routes.size
    val rt = routes.map{ it.toSet() }
    val edges = (0 until n).map{ mutableListOf<Int>() }
    val que = LinkedList<Pair<Int, Int>>()
    for(i in 0 until n){
      if(S in rt[i]) que.push(1 to i)
      for(j in i+1 until n)
        if(routes[i].any{it in rt[j]}) {
          edges[i].add(j)
          edges[j].add(i)
        }
    }

    val done = que.map{it.second}.toMutableSet()
    while(que.isNotEmpty()){
      val (cnt, i) = que.pollLast()
      if(T in rt[i]) return cnt
      for(j in edges[i])
        if(j !in done) {
          done.add(j)
          que.push(cnt + 1 to j)
        }
    }

    return -1
  }

  @Test
  fun test1(){
    assertEquals(2, numBusesToDestination(arrayOf(intArrayOf(1, 2, 7), intArrayOf(3, 6, 7)), 1, 6))
  }
}