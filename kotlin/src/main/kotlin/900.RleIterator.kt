import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/rle-iterator


class RLEIterator(val A: IntArray) {
  var cnt = 0
  var i = 0
  var n = A.size

  fun next(m: Int): Int {
    var k = m
    while(k > 0 && i < n){
      val dis = minOf(k, A[i] - cnt)
      k -= dis
      cnt += dis
      if(k > 0){
        i += 2
        cnt = 0
      }
    }
    return if(k > 0) -1 else A[i+1]
  }
}

class RLEIteratorTests{
  @Test
  fun test1(){
    val it = RLEIterator(intArrayOf(3,8,0,9,2,5))
    assertEquals(8, it.next(2))
    assertEquals(8, it.next(1))
    assertEquals(5, it.next(1))
    assertEquals(-1, it.next(2))
  }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = RLEIterator(A)
 * var param_1 = obj.next(n)
 */

