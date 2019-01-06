import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/binary-search-tree-iterator/

class BinarySearchTreeIterator(root: TreeNode?) {
  private val middles = Stack<TreeNode>()

  init {
    parse(root)
  }

  private fun parse(nd: TreeNode?) {
    var node = nd
    while (node != null) {
      middles.push(node)
      node = node.left
    }
  }

  /** @return the next smallest number */
  fun next(): Int {
    val node = middles.pop()
    parse(node.right)
    return node.`val`
  }

  /** @return whether we have a next smallest number */
  fun hasNext() = middles.isNotEmpty()

}

class BinarySearchTreeIteratorTests{
  @Test
  fun test1(){
    val root = TreeNode(7).also {
      it.left = TreeNode(3)
      it.right = TreeNode(15).also {
        it.left = TreeNode(9)
        it.right = TreeNode(20)
      }
    }

    val iterator = BinarySearchTreeIterator(root)
    assertEquals(3, iterator.next())
    assertEquals(7, iterator.next())
    assertEquals(true, iterator.hasNext())
    assertEquals(9, iterator.next())
    assertEquals(15, iterator.next())
    assertEquals(true, iterator.hasNext())
    assertEquals(20, iterator.next())
    assertEquals(false, iterator.hasNext())
  }

}