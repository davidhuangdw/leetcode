import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/binary-tree-paths/


class BinaryTreePaths{
  fun binaryTreePaths(root: TreeNode?): List<String> {
    val ret = mutableListOf<String>()
    fun dfs(node: TreeNode?, path: List<Int>){
      if(node == null) return

      val p = path + listOf(node.`val`)
      if(node.left == null && node.right == null)
        ret.add(p.joinToString("->"))
      dfs(node.left, p)
      dfs(node.right, p)
    }
    dfs(root, emptyList())
    return ret
  }

  @Test
  fun test1(){
    val root = TreeNode(1).also{
      it.left = TreeNode(2).also { it.right = TreeNode(5) }
      it.right = TreeNode(3)
    }
    assertEquals(listOf("1->2->5", "1->3"), binaryTreePaths(root))
  }

  @Test
  fun test2(){
    assertEquals(listOf<String>(), binaryTreePaths(null))
  }
}