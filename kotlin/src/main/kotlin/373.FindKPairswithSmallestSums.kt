import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/find-k-pairs-with-smallest-sums/


class FindKPairswithSmallestSums{
  fun kSmallestPairs(nums1: IntArray, nums2: IntArray, k: Int): List<IntArray> {
    val ret = mutableListOf<IntArray>()
    if(k == 0 || nums1.isEmpty() || nums2.isEmpty()) return ret
    val que = PriorityQueue<IntArray>(compareBy{ nums1[it[0]] + nums2[it[1]] })
    que.add(intArrayOf(0, 0))
    while (que.isNotEmpty() && ret.size < k){
      val minPair = que.poll()
      val (i, j) = minPair
      ret.add(intArrayOf(nums1[i], nums2[j]))
      if(j+1 < nums2.size) que.add(intArrayOf(i, j+1))
      if(j == 0 && i+1 < nums1.size) que.add(intArrayOf(i+1, j))
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(listOf(intArrayOf(1,2), intArrayOf(1,4), intArrayOf(1,6)).map{it.toList()},
        kSmallestPairs(intArrayOf(1,7,11), intArrayOf(2,4,6), 3).map{it.toList()})
  }

  @Test
  fun test2(){
    assertEquals(listOf(intArrayOf(1,1), intArrayOf(1,1)).map{it.toList()},
        kSmallestPairs(intArrayOf(1,1,2), intArrayOf(1,2,3), 2).map{it.toList()})
  }

  @Test
  fun test3(){
    assertEquals(listOf(intArrayOf(1,3), intArrayOf(2,3)).map{it.toList()},
        kSmallestPairs(intArrayOf(1,2), intArrayOf(3), 3).map{it.toList()})
  }
}