import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/count-complete-tree-nodes


/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class CountCompleteTreeNodes {
  fun height(node: TreeNode?): Int = if(node == null) 0 else 1 + height(node.left)
  fun fullCount(h: Int) = (1 shl h) - 1
  fun countNodes(root: TreeNode?): Int {
    if(root == null) return 0
    val h = height(root.left)
    return if(height(root.right) == h)
      1 + fullCount(h) + countNodes(root.right)
    else
      1 + countNodes(root.left) + fullCount(h-1)
  }

  @Test
  fun test1(){
    val root = TreeNode()
    root.left = TreeNode()
    root.left!!.left = TreeNode()
    root.left!!.right = TreeNode()
    root.right = TreeNode()
    root.right!!.left = TreeNode()
    assertEquals(6, countNodes(root))
  }
}

