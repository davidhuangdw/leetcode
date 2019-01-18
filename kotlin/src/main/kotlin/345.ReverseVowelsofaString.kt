import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/reverse-vowels-of-a-string/


class ReverseVowelsofaString{
  fun reverseVowels(s: String): String {
    val vowels = "aeiouAEIOU"
    val inds = (0 until s.length).filter{ s[it] in vowels }
    var (l, r) = 0 to inds.size-1
    val sl = s.toMutableList()
    while(l < r){
      val t = sl[inds[l]]
      sl[inds[l++]] = sl[inds[r]]
      sl[inds[r--]] = t
    }
    return sl.joinToString("")
  }

  @Test
  fun test1(){
    assertEquals("holle", reverseVowels("hello"))
  }

  @Test
  fun test2(){
    assertEquals("leotcede", reverseVowels("leetcode"))
  }
}