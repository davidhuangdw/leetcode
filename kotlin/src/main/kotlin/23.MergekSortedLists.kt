import ListNode.Companion.buildFromList
import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/merge-k-sorted-lists/

class MergekSortedLists {
  fun mergeKLists(lists: Array<ListNode?>): ListNode? {
    val que = PriorityQueue<ListNode>{x: ListNode, y:ListNode -> x.`val` - y.`val`}

    for(node in lists)
      if(node != null) que.add(node)

    val head = ListNode(0)
    var tail: ListNode = head
    while(!que.isEmpty()){
      var node = que.poll()
      tail.next = node
      node = node.next
      tail = tail.next!!
      if(node != null) que.add(node)
    }

    return head.next
  }

  @Test
  fun test1(){
    assertEquals(listOf(1,1,2,3,4,4,5,6), mergeKLists(arrayOf(
        buildFromList(1,4,5),
        buildFromList(1,3,4),
        buildFromList(2,6)
    ))!!.asList())
  }
}