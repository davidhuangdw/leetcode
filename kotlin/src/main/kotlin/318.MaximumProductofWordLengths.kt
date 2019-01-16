import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/maximum-product-of-word-lengths/


class MaximumProductofWordLengths{
  private fun bits(word: String): Int{
    var ret = 0
    for(ch in word)
      ret = ret or (1 shl (ch.toInt() - 'a'.toInt()))
    return ret
  }

  fun maxProduct(words: Array<String>): Int {
    val bs = words.map{ bits(it) }
    val n = words.size
    var ret = 0
    for(i in 0 until n)
      for(j in i+1 until n)
        if(bs[i] and bs[j] == 0)
          ret = maxOf(ret, words[i].length * words[j].length)
    return ret
  }

  @Test
  fun test1(){
    assertEquals(16, maxProduct(arrayOf("abcw","baz","foo","bar","xtfn","abcdef")))
  }

  @Test
  fun test2(){
    assertEquals(0, maxProduct(arrayOf("a","aa","aaa","aaaa")))
  }
}