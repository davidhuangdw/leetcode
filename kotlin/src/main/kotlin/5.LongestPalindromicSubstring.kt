import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/longest-palindromic-substring


class LongestPalindromicSubstring {
  fun longestPalindrome(s: String): String {
    val sharped = mutableListOf('#')
    for(ch in s){
      sharped.add(ch)
      sharped.add('#')
    }

    var (mx, n) = 0 to sharped.size
    val ends = IntArray(n) // right end of the palindrome centered at i
    var (m, r) = -1 to 0

    for(i in 0 until sharped.size){
      var j = i+1
      if(j < r){
        val pre = 2*m - i
        j = minOf(r,i + (ends[pre] - pre))
      }
      while(j < n && 2*i -j >=0 && sharped[2*i-j] == sharped[j])
        j ++
      ends[i] = j
      if(j - i > ends[mx] -mx)
        mx = i
      if(j > r){
        m = i
        r = j
      }
    }
    return sharped.slice(2*mx-ends[mx]+1 until ends[mx])
            .filter{ it != '#'}.joinToString("")
  }

  @Test
  fun test1(){
    assertEquals("bab", longestPalindrome("babad"))
  }

  @Test
  fun test2(){
    assertEquals("bb", longestPalindrome("cbbd"))
  }

}

