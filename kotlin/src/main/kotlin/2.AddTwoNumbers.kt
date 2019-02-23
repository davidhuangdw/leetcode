import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/add-two-numbers


/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class AddTwoNumbers {
  fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
    var (p1, p2) = l1 to l2
    val head = ListNode(0)
    var tail = head
    var add = 0
    while(p1 != null || p2 != null || add > 0){
      val sum = add + (p1?.`val` ?: 0) + (p2?.`val` ?: 0)
      tail.next = ListNode(sum % 10)
      add = sum / 10
      tail = tail.next!!
      p1 = p1?.next
      p2 = p2?.next
    }
    return head.next
  }

  @Test
  fun test1(){
    assertEquals(listOf(7, 0, 8, 1), addTwoNumbers(
        ListNode.buildFromList(2,4,3),
        ListNode.buildFromList(5,6,4,1)
    )!!.asList())
  }

  @Test
  fun test2(){
    assertEquals(listOf(0, 1), addTwoNumbers(
        ListNode.buildFromList(5),
        ListNode.buildFromList(5)
        )!!.asList())
  }
}

