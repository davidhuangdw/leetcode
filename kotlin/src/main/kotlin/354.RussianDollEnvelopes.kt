import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/russian-doll-envelopes/


class RussianDollEnvelopes{
  fun maxEnvelopes(envelopes: Array<IntArray>): Int {
    var ret = 0
    val sorted = envelopes.sortedWith(compareBy({it[0]}, {-it[1]})).map{it[1]}
    val n = envelopes.size
    val mins = IntArray(n+1){ Int.MAX_VALUE }
    mins[0] = Int.MIN_VALUE

    for(h in sorted){
      var (l, r) = 0 to n
      while(l <= r){
        val m = (l+r)/2
        if(mins[m] < h)
          l = m+1
        else
          r = m-1
      }
      mins[l] = h
      ret = maxOf(ret, l)
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(3, maxEnvelopes(arrayOf(
        intArrayOf(5,4),
        intArrayOf(6,4),
        intArrayOf(6,7),
        intArrayOf(2,3))))
  }
}