import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/sum-of-distances-in-tree/


class SumofDistancesinTree{
  fun sumOfDistancesInTree(N: Int, edges: Array<IntArray>): IntArray {
    val e = (1..N).map{ mutableListOf<Int>() }
    for((i,j) in edges){
      e[i].add(j)
      e[j].add(i)
    }

    val cnt = (1..N).map{ 0 }.toMutableList()
    fun dfs(i: Int, parent: Int): Int{
      var sum = 0
      cnt[i] = 1
      for(j in e[i])
        if(j != parent){
          sum += dfs(j, i) + cnt[j]
          cnt[i] += cnt[j]
        }
      return sum
    }
    val res = IntArray(N)
    fun cal(i: Int, parent: Int){
      for(j in e[i])
        if(j != parent){
          res[j] = res[i] + N - cnt[j] * 2
          cal(j, i)
        }
    }
    res[0] = dfs(0, -1)
    cal(0, -1)
    return res
  }

  @Test
  fun test1(){
    assertEquals(listOf(8,12,6,10,10,10), sumOfDistancesInTree(6, arrayOf(
        intArrayOf(0,1),
        intArrayOf(0,2),
        intArrayOf(2,3),
        intArrayOf(2,4),
        intArrayOf(2,5)
    )).toList())
  }

}