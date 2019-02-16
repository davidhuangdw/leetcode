import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/subarrays-with-k-different-integers/


class SubarrayswithKDifferentIntegers{
  data class MultiSet(var size: Int = 0){
    val cnt = hashMapOf<Int, Int>()
    fun add(v: Int){
      cnt[v] = cnt.getOrDefault(v, 0) + 1
      if(cnt[v] == 1)
        size ++
    }
    fun remove(v: Int){
      cnt[v] = cnt[v]!! - 1
      if(cnt[v] == 0)
        size --
    }
  }

  fun subarraysWithKDistinct(A: IntArray, K: Int): Int {
    var (j, k) = 0 to 0
    val (sj, sk) = MultiSet() to MultiSet()
    var res = 0
    for((i, v) in A.withIndex()){
      sj.add(v)
      sk.add(v)
      while(sj.size > K)
        sj.remove(A[j++])
      while(sk.size >= K)
        sk.remove(A[k++])
      res += k - j
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(7, subarraysWithKDistinct(intArrayOf(1,2,1,2,3), 2))
  }

  @Test
  fun test2(){
    assertEquals(3, subarraysWithKDistinct(intArrayOf(1,2,1,3,4), 3))
  }
}