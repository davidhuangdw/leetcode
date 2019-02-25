import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

// https://leetcode.com/problems/kth-largest-element-in-an-array


class KthLargestElementInAnArray {
  fun findKthLargest(nums: IntArray, k: Int): Int {
    val que = PriorityQueue<Int>(compareByDescending{ it })
    que.addAll(nums.toList())
    for(i in 1 until k)
      que.poll()
    return que.peek()!!
  }

  @Test
  fun test1() {
    assertEquals(5, findKthLargest(intArrayOf(3, 2, 1, 5, 6, 4), 2))
  }

  @Test
  fun test2(){
    assertEquals(4, findKthLargest(intArrayOf(3,2,3,1,2,4,5,5,6), 4))
  }

}

