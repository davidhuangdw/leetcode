import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/couples-holding-hands/


class CouplesHoldingHands{
  fun minSwapsCouples(row: IntArray): Int {
    val index = hashMapOf<Int, Int>()
    for((i, v) in row.withIndex())
      index[v] = i

    var count = 0
    for(i in 0 until row.size step 2){
      val a = row[i]
      val b = a xor 1
      if(index[b] != i+1){
        count ++
        index[row[i+1]] = index[b]!!
        row[index[b]!!] = row[i+1]
      }
    }
    return count
  }

  @Test
  fun test1(){
    assertEquals(1, minSwapsCouples(intArrayOf(0, 2, 1, 3)))
  }

  @Test
  fun test2(){
    assertEquals(0, minSwapsCouples(intArrayOf(3, 2, 0, 1)))
  }
}