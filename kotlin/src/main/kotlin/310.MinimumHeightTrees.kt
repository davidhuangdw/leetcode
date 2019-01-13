import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/minimum-height-trees/
import java.util.*


class MinimumHeightTrees{
  // topo order: leaves layer by layer
  fun findMinHeightTrees(n: Int, edges: Array<IntArray>): List<Int> {
    val remains = (0 until n).toMutableSet()
    val linked = (0 until n).map{ mutableListOf<Int>()}.toList()
    val degree = IntArray(n)

    for((i,j) in edges){
      degree[i] ++
      degree[j] ++
      linked[i].add(j)
      linked[j].add(i)
    }
    var leaves = LinkedList((0 until n).filter{ degree[it] == 1})

    while(remains.size > 2){
      val next = LinkedList<Int>()
      while(leaves.isNotEmpty()){
        val lf = leaves.pop()
        remains.remove(lf)

        for(ch in linked[lf]){
          degree[ch] --
          if(degree[ch] == 1)
            next.add(ch)
        }
      }
      leaves = next
    }
    return remains.toList()
  }

  @Test
  fun test1(){
    assertEquals(listOf(1), findMinHeightTrees(4, arrayOf(
        intArrayOf(1, 0),
        intArrayOf(1, 2),
        intArrayOf(1, 3)
    )))
  }

  @Test
  fun test2(){
    assertEquals(listOf(3, 4), findMinHeightTrees(6, arrayOf(
        intArrayOf(0, 3),
        intArrayOf(1, 3),
        intArrayOf(2, 3),
        intArrayOf(4, 3),
        intArrayOf(4, 5)
    )))
  }
}