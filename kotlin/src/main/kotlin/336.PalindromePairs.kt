import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/palindrome-pairs/


class PalindromePairs{
  fun palindromePairs(words: Array<String>): List<List<Int>> {
    val ind = HashMap<String, Int>()
    for((i, w) in words.withIndex())
      ind[w] = i

    fun isPal(word: String) = word.reversed() == word

    val ret = mutableListOf<List<Int>>()
    for((i, word) in words.withIndex()){
      for(k in 0 until word.length+1){
        if(isPal(word.substring(k))) {
          val j = ind.getOrDefault(word.substring(0, k).reversed(), -1)
          if(j >= 0 && j != i)
            ret.add(listOf(i, j))
        }
        if(k > 0 && isPal(word.substring(0, k))){
          val j = ind.getOrDefault(word.substring(k).reversed(), -1)
          if(j >= 0 && j != i)
            ret.add(listOf(j, i))
        }
      }
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(listOf(
        listOf(0,1),
        listOf(1,0),
        listOf(3,2),
        listOf(2,4)
    ), palindromePairs(arrayOf("abcd","dcba","lls","s","sssll")))
  }

  @Test
  fun test2(){
    assertEquals(listOf(
        listOf(0,1),
        listOf(1,0)
    ), palindromePairs(arrayOf("bat","tab","cat")))
  }

  @Test
  fun test3(){
    assertEquals(listOf(
        listOf(3,0),
        listOf(1,3),
        listOf(4,0),
        listOf(2,4),
        listOf(5,0),
        listOf(0,5)
    ), palindromePairs(arrayOf("a","b","c","ab","ac","aa")))
  }
}