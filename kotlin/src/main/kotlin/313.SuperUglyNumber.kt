import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/super-ugly-number/

import java.util.*
class SuperUglyNumber{
  fun nthSuperUglyNumber(n: Int, primes: IntArray): Int {
    val nums = mutableListOf(1)
    val heads = primes.map{0}.toMutableList()
    fun next(i: Int) = primes[i]*nums[heads[i]]
    val que = PriorityQueue<Int>(compareBy{next(it)})
    for(i in 0 until primes.size)
      que.add(i)

    while(nums.size < n){
      val i = que.poll()
      val nxt = next(i)
      if(nxt > nums.last())
        nums.add(nxt)
      heads[i]++
      que.add(i)
    }
    return nums.last()
  }

  @Test
  fun test1(){
    assertEquals(32, nthSuperUglyNumber(12, intArrayOf(2,7,13,19)))
  }
}