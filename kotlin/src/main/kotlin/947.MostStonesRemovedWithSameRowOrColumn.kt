import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column


class MostStonesRemovedWithSameRowOrColumn {
  fun removeStones(stones: Array<IntArray>): Int {
    val parent = hashMapOf<Int, Int>()
    fun find(v: Int): Int{
      if(v !in parent)
        parent[v] = v
      else if(parent[v] != v)
        parent[v] = find(parent[v]!!)
      return parent[v]!!
    }
    for((i, j) in stones)
      parent[find(i)] = find(-1-j)

    val res = mutableSetOf<Int>()
    for((i, _) in stones)
      res.add(find(i))
    return stones.size - res.size
  }

  @Test
  fun test1(){
    assertEquals(5, removeStones(arrayOf(
        intArrayOf(0,0),
        intArrayOf(0,1),
        intArrayOf(1,0),
        intArrayOf(1,2),
        intArrayOf(2,1),
        intArrayOf(2,2)
    )))
  }

  @Test
  fun test2(){
    assertEquals(3, removeStones(arrayOf(
        intArrayOf(0,0),
        intArrayOf(0,2),
        intArrayOf(1,1),
        intArrayOf(2,0),
        intArrayOf(2,2)
        )))
  }

}

