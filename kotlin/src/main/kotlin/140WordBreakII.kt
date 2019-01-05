import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/word-break-ii/

class WordBreakII{
  fun wordBreak(s: String, wordDict: List<String>): List<String> {
    val mxlen = wordDict.map(String::length).max() ?: 0
    val words = wordDict.toHashSet()

    val n = s.length
    val pre = (1..n).map{ mutableListOf<Int>() }

    for(i in 0 until n){
      if(i!=0 && pre[i-1].isEmpty()) continue
      for(j in i until minOf(n, i+mxlen)){
        if(s.substring(i..j) in words)
          pre[j].add(i-1)
      }
    }


    val result = mutableListOf<String>()
    fun build(j: Int, backwards: List<String>){
      if(j==-1)
        result.add(backwards.reversed().joinToString(" "))
      else
        for(i in pre[j])
          build(i, backwards + listOf(s.substring(i+1..j)))
    }

    build(n-1, listOf())
    return result.reversed()
  }

  @Test
  fun test1(){
    assertEquals(listOf(
        "cats and dog",
        "cat sand dog"), wordBreak("catsanddog", listOf("cat", "cats", "and", "sand", "dog")))
  }

  @Test
  fun test2(){
    assertEquals(listOf(
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"), wordBreak("pineapplepenapple", listOf("apple", "pen", "applepen", "pine", "pineapple")))
  }

  @Test
  fun test3(){
    assertEquals(listOf<String>(
       ), wordBreak("catsandog", listOf("cats", "dog", "sand", "and", "cat")))
  }

}