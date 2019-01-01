import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/wildcard-matching/

class WildcardMatching{
  fun isMatch(s: String, p: String): Boolean {
    val n = s.length
    val mat = BooleanArray(n+1)
    mat[0] = true

    for(pi in p)
      if(pi == '*') {
        for (j in 0 until n)
          mat[j+1] = mat[j+1] || mat[j]
      }else{
        for(j in n-1 downTo 0)
          mat[j+1] = mat[j] && (pi=='?' || pi==s[j])
        mat[0] = false
      }

    return mat[n]
  }

  @Test
  fun test1(){
    assertEquals(false, isMatch("aa", "a"))
  }

  @Test
  fun test2(){
    assertEquals(true, isMatch("aa", "*"))
  }

  @Test
  fun test3(){
    assertEquals(false, isMatch("cb", "?a"))
  }

  @Test
  fun test4(){
    assertEquals(true, isMatch("adceb", "*a*b"))
  }

  @Test
  fun test5(){
    assertEquals(false, isMatch("acdcb", "a*c?b"))
  }
}