import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/linked-list-random-node/


class LinkedListRandomNode{
  class Solution(val head: ListNode?) {

    /** @param head The linked list's head.
    Note that the head is guaranteed to be not null, so it contains at least one node. */

    val rand = Random()

    /** Returns a random node's value. */
    fun getRandom(): Int {
      if(head == null) return -1
      var cur = head!!
      var chosen = cur
      var len = 1
      while(cur.next != null){
        cur = cur.next!!
        len += 1
        if(rand.nextInt(len) == 0)
          chosen = cur
      }
      return chosen.`val`
    }

  }
}