import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/kth-smallest-element-in-a-bst/


class KthSmallestElementBST{
  fun kthSmallest(root: TreeNode?, k: Int): Int {
    var count = 0
    var ret: Int? = null
    val middles = Stack<TreeNode>()

    fun decompose(nd: TreeNode?){
      var node = nd
      while(node != null){
        middles.push(node)
        node = node.left
      }
    }

    decompose(root)
    while(!middles.empty()){
      val node = middles.pop()
      count ++
      if(count == k){
        ret = node.`val`
        break
      }
      decompose(node.right)
    }
    return ret!!
  }

  @Test
  fun test1(){
    val root = TreeNode(3).also {
      it.left = TreeNode(1).also { it.right = TreeNode(2) }
      it.right = TreeNode(4)
    }
    assertEquals(1, kthSmallest(root, 1))
  }

  @Test
  fun test2(){
    val root = TreeNode(5).also {
      it.left = TreeNode(3).also {
        it.left = TreeNode(2).also { it.left = TreeNode(1) }
        it.right = TreeNode(4)
      }
      it.right = TreeNode(6)
    }
    assertEquals(3, kthSmallest(root, 3))
  }

}