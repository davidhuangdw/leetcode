import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/swap-adjacent-in-lr-string


class SwapAdjacentInLrString {
  fun canTransform(start: String, end: String): Boolean {
    var (nr, nl) = 0 to 0
    if(start.length != end.length) return false
    for(i in 0 until start.length){
      val (sc, ec) = start[i] to end[i]
      if(ec == 'L') nl++
      if(sc == 'R') nr++
      if(nl > 0 && nr > 0) return false
      if(sc == 'L') nl--
      if(ec == 'R') nr--
      if(nl < 0 || nr < 0) return false
    }
    return nl==0 && nr==0
  }

  @Test
  fun test1(){
    assertEquals(true, canTransform("RXXLRXRXL", "XRLXXRRLX"))
  }

  @Test
  fun test2(){
    assertEquals(true, canTransform("XLXRRXXRXX", "LXXXXXXRRR"))
  }

}

