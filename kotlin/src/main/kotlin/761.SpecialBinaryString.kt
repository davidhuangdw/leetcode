import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/special-binary-string/


class SpecialBinaryString{
  fun makeLargestSpecial(S: String): String {
    if(S.isEmpty()) return S
    val n = S.length
    var i = 0
    val mountains = mutableListOf<String>()
    while(i < n){
      var j = i+1
      var cnt = 1
      while(cnt > 0){
        cnt += if(S[j] == '1') 1 else -1
        j += 1
      }
      mountains.add("1${makeLargestSpecial(S.slice(i+1 until j-1))}0")
      i = j
    }
    mountains.sortDescending()
    return mountains.joinToString("")
  }

  @Test
  fun test1(){
    assertEquals("11100100", makeLargestSpecial("11011000"))
  }
}