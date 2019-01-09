import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/h-index/


class HIndex{
  fun hIndex(citations: IntArray): Int {
    val n = citations.size
    val cnt = IntArray(n+1)
    for(c in citations)
      cnt[minOf(c, n)] ++
    var sum = 0
    for(i in n downTo 1){
      sum += cnt[i]
      if(sum >= i)
        return i
    }
    return 0
  }

  @Test
  fun test1(){
    assertEquals(3, hIndex(intArrayOf(3,0,6,1,5)))
  }

  @Test
  fun test2(){
    assertEquals(0, hIndex(intArrayOf()))
  }
}