import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/shortest-palindrome/


class ShortestPalindrome{
    fun shortestPalindrome(s: String): String {
      val constr = "$s#${s.reversed()}"
      val f = IntArray(constr.length)
      for(i in 1 until constr.length) {
        var j = f[i-1]
        while(j > 0 && constr[j] != constr[i])
          j = f[j-1]
        f[i] = if(constr[j]==constr[i]) j+1 else 0
      }
      return s.substring(f.last()).reversed() + s
    }

//  fun kmpLen(s: String): List<Int>{
//    val longest = IntArray(s.length)
//    for(i in 1 until s.length){
//      var j = longest[i-1]
//      while(j > 0 && s[j] != s[i])
//        j = longest[j-1]
//      longest[i] = if(s[j] == s[i]) j+1 else 0
//    }
//    return longest.toList()
//  }
//
//  fun shortestPalindrome(s: String): String {
//    val longest = kmpLen(s.substring(0, s.length/2))
//    var l = 0
//    var r = s.length-1
//    while(l < r) {
//      if (s[l] == s[r]) {
//        l++
//        r--
//      } else if (l > 0)
//        l = longest[l-1]
//      else
//        r--
//    }
//    val parLen = if(l==r) l*2+1 else l*2
//    return s.substring(parLen).reversed() + s
//  }

  @Test
  fun test1(){
    assertEquals("aaacecaaa", shortestPalindrome("aacecaaa"))
  }

  @Test
  fun test2(){
    assertEquals("dcbabcd", shortestPalindrome("abcd"))
  }

  @Test
  fun test3(){
    assertEquals("", shortestPalindrome(""))
  }
}