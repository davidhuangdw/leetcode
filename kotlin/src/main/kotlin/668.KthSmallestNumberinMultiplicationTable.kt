import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


class KthSmallestNumberinMultiplicationTable{
  fun findKthNumber(m: Int, n: Int, k: Int): Int {
    fun count(v: Long): Int{
      var t = n
      var c = 0
      for(i in 1..m){
        var mul = i*t
        while(mul > v){
          mul -= i
          t --
        }
        c += t
      }
      return c
    }

    var (l, r) = 1L to m.toLong()*n
    while(l <= r){
      val md = (r-l)/2+l
      if(count(md) >= k)
        r = md - 1
      else
        l = md + 1
    }
    return l.toInt()
  }

  @Test
  fun test1(){
    assertEquals(3, findKthNumber(3,3,5))
  }

  @Test
  fun test2(){
    assertEquals(6, findKthNumber(2,3,6))
  }
}