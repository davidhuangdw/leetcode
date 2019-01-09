import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/sliding-window-maximum/


class SlidingWindowMaximum{
  class MaxQue{
    val values = LinkedList<Int>()
    private val maxes = LinkedList<Int>()

    fun max() = maxes.last
    fun add(v: Int){
      while (maxes.isNotEmpty() && maxes.peek() < v)
        maxes.pop()
      maxes.push(v)
      values.push(v)
    }
    fun remove() = values.removeLast()
        .also { if(it == maxes.last) maxes.removeLast() }
  }

  fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
    if(k==0) return intArrayOf()
    val que = MaxQue()
    val n = nums.size

    for(i in 0 until minOf(n,k))
      que.add(nums[i])

    val result = mutableListOf(que.max())
    for(i in k until n){
      que.remove()
      que.add(nums[i])
      result.add(que.max())
    }
    return result.toIntArray()
  }

  @Test
  fun test1(){
    assertEquals(intArrayOf(3,3,5,5,6,7).toList(), maxSlidingWindow(intArrayOf(1,3,-1,-3,5,3,6,7), 3).toList())
  }

}