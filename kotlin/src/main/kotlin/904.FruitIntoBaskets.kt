import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/fruit-into-baskets


class FruitIntoBaskets {
  fun totalFruit(tree: IntArray): Int {
    var max = 0
    val count = hashMapOf<Int, Int>()
    var j = 0
    for((i, v) in tree.withIndex()){
      count[v] = count.getOrDefault(v, 0) + 1
      while(count.size > 2){
        val vj = tree[j]
        count[vj] = count[vj]!! - 1
        if(count[vj]!! == 0)
          count.remove(vj)
        j ++
      }
      max = maxOf(max, i-j+1)
    }
    return max
  }

  @Test
  fun test1(){
    assertEquals(3, totalFruit(intArrayOf(1,2,1)))
  }

  @Test
  fun test2(){
    assertEquals(3, totalFruit(intArrayOf(0,1,2,2)))
  }

  @Test
  fun test3(){
    assertEquals(5, totalFruit(intArrayOf(3,3,3,1,2,1,1,2,3,3,4)))
  }

}
