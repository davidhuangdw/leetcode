import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/frog-jump/


class FrogJump{
  fun canCross(stones: IntArray): Boolean {
    val n = stones.size
    val indexes = HashMap<Int, Int>()
    for((i,s) in stones.withIndex())
      indexes[s] = i

    val tried = HashSet<Pair<Int, Int>>()
    fun dp(i: Int, k: Int): Boolean{
      if(i == n-1) return true
      if(tried.contains(i to k)) return false
      tried.add(i to k)
      for(nk in k-1..k+1)
        if(nk > 0 && indexes.contains(stones[i]+nk) && dp(indexes[stones[i]+nk]!!, nk))
          return true
      return false
    }
    return stones[1] == 1 && dp(1, 1)
  }

  @Test
  fun test1(){
    assertEquals(true, canCross(intArrayOf(0,1,3,5,6,8,12,17)))
  }

  @Test
  fun test2(){
    assertEquals(false, canCross(intArrayOf(0,1,2,3,4,8,9,11)))
  }
}