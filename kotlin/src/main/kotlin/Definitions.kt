class ListNode(var `val`: Int = 0) {
  var next: ListNode? = null

  fun asList(): List<Int>{
    val result = mutableListOf<Int>(`val`)
    var node = next
    while(node != null) {
      result.add(node.`val`)
      node = node.next
    }
    return result
  }

  companion object {
    fun buildFromList(vararg values: Int): ListNode?{
      val head = ListNode()
      for(v in values.reversed()) {
        val node = ListNode(v)
        node.next = head.next
        head.next = node
      }
      return head.next
    }
  }
}

class Interval(
    var start: Int = 0,
    var end: Int = 0
){
  fun asPair(): Pair<Int, Int>{
    return Pair(start, end)
  }
}

class TreeNode(var `val`: Int = 0) {
  var left: TreeNode? = null
  var right: TreeNode? = null
}
