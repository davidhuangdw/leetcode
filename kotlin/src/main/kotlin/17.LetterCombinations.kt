import org.junit.Assert
import org.junit.Test

// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

val LETTERS = listOf(
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
)

class LetterCombinations{
  fun letterCombinations(digits: String): List<String> {
    val result = mutableListOf<String>()

    fun build(prefix: String, i: Int){
      if(i == digits.length)
        result.add(prefix)
      else{
        val j = digits[i].toInt() - '2'.toInt()
        for(c in LETTERS[j])
          build(prefix+c, i+1)
      }
    }

    if(digits.isNotEmpty())
      build("", 0)
    return result
  }


  @Test
  fun test1(){
    Assert.assertEquals(listOf("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"), letterCombinations("23"))
  }

  @Test
  fun blank(){
    Assert.assertEquals(listOf<String>(), letterCombinations(""))
  }
}
