import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/backspace-string-compare


class BackspaceStringCompare {
  private fun next(s: String, idx: Int): Int{
    var (i, c) = idx to 0
    while(i >= 0 && (s[i] == '#' || c > 0))
      c += if(s[i--] == '#') 1 else -1
    return i
  }
  fun backspaceCompare(S: String, T: String): Boolean {
    var (i, j) = S.length-1 to T.length-1
    while(true){
      i = next(S, i)
      j = next(T, j)
      if(i < 0 || j < 0)
        return i == j
      if(S[i--] != T[j--])
        return false
    }
  }

  @Test
  fun test1(){
    assertEquals(true, backspaceCompare("ab#c", "ad#c"))
  }

  @Test
  fun test2(){
    assertEquals(true, backspaceCompare("a##c", "#a#c"))
  }

  @Test
  fun test3(){
    assertEquals(false, backspaceCompare("a#c", "b"))
  }
}

