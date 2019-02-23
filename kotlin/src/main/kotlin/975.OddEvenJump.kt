import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

// https://leetcode.com/problems/odd-even-jump


class OddEvenJump {
  fun oddEvenJumps(A: IntArray): Int {
    var (res, n) = 1 to A.size
    val order = TreeSet<Pair<Int, Int>>(compareBy({it.second}, {it.first}))
    val good = hashMapOf<Int, Pair<Boolean, Boolean>>()
    order.add(n-1 to A[n-1])
    good[n-1] = true to true
    for(i in n-2 downTo 0){
      val v = A[i]
      val r = order.ceiling(i to v)
      val odd = r != null && good[r.first]!!.second
      var l = order.floor(n to v)
      if(l != null)
        l = order.ceiling(0 to l.second)
      val even = l != null && good[l.first]!!.first
      if(odd) res ++
      good[i] = odd to even
      order.add(i to v)
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(2, oddEvenJumps(intArrayOf(10,13,12,14,15)))
  }

  @Test
  fun test2(){
    assertEquals(3, oddEvenJumps(intArrayOf(2,3,1,1,4)))
  }

  @Test
  fun test3(){
    assertEquals(3, oddEvenJumps(intArrayOf(5,1,3,4,2)))
  }
}

