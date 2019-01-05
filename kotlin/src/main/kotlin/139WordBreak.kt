import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/word-break/

class WordBreak{
  fun wordBreak(s: String, wordDict: List<String>): Boolean {
    val words = wordDict.toHashSet()
    val mxlen = words.map(String::length).max() ?: 0
    val n = s.length
    val reach = (0..n).map{ false }.toMutableList()
    reach[0] = true

    for(l in 0 until n) {
      if(!reach[l]) continue
      for (r in l until minOf(n, l+mxlen))
        if(!reach[r+1] && words.contains(s.substring(l..r)))
          reach[r+1] =true
    }

    return reach[n]
  }

  @Test
  fun test1(){
    assertEquals(true, wordBreak("leetcode", listOf("leet", "code")))
  }

  @Test
  fun test2(){
    assertEquals(true, wordBreak("applepenapple", listOf("apple", "pen")))
  }

  @Test
  fun test3(){
    assertEquals(false, wordBreak("catsandog", listOf("cats", "dog", "sand", "and", "cat")))
  }

  @Test
  fun test4(){
    assertEquals(true, wordBreak("a", listOf("a")))
  }

}